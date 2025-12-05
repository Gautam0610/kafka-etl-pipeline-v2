import psycopg2
import json

class PostgresSink:
    def __init__(self, dbname, user, password, host, port, table_name):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.table_name = table_name
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, user=self.user, password=self.password,
                host=self.host, port=self.port
            )
            self.cursor = self.conn.cursor()
            print("Connected to Postgres.")
        except psycopg2.Error as e:
            print(f"Error connecting to Postgres: {e}")
            return False
        return True

    def create_table(self, data_sample):
        if not isinstance(data_sample, dict):
            print("Data sample must be a dictionary.")
            return False

        columns = []
        for key, value in data_sample.items():
            if isinstance(value, int):
                columns.append(f"{key} INTEGER")
            elif isinstance(value, float):
                columns.append(f"{key} FLOAT")
            else:
                columns.append(f"{key} TEXT")

        column_str = ", ".join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({column_str})"

        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()
            print(f"Table {self.table_name} created.")
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")
            return False
        return True

    def insert_data(self, data):
        if not isinstance(data, dict):
            print("Data must be a dictionary.")
            return False

        columns = ", ".join(data.keys())
        values = ", ".join([self.adapt_value(value) for value in data.values()])
        insert_query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({values})"

        try:
            self.cursor.execute(insert_query)
            self.conn.commit()
            print("Data inserted successfully.")
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")
            return False
        return True

    def adapt_value(self, value):
        if value is None:
            return "NULL"
        if isinstance(value, (int, float)):
            return str(value)
        return f"'{str(value).replace("'", "''")}'"  # Escape single quotes

    def sink(self, data):
        if not self.conn:
            print("Not connected to Postgres.")
            return False

        if not hasattr(self, 'table_created'):
            if not self.create_table(data[0] if isinstance(data, list) else data):
                return False
            self.table_created = True

        if isinstance(data, list):
            for item in data:
                if not self.insert_data(item):
                    return False
        else:
            if not self.insert_data(data):
                return False
        return True

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Postgres connection closed.")

if __name__ == '__main__':
    # Example Usage
    postgres_sink = PostgresSink(
        dbname='your_dbname',
        user='your_user',
        password='your_password',
        host='localhost',
        port='5432',
        table_name='your_table'
    )

    if postgres_sink.connect():
        data = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
        postgres_sink.sink(data)
        postgres_sink.close()
