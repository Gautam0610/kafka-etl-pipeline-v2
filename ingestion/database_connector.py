import psycopg2
from kafka import KafkaProducer
import json

class DatabaseConnector:
    def __init__(self, bootstrap_servers, topic, dbname, user, password, host, port, query):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.query = query
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, user=self.user, password=self.password,
                host=self.host, port=self.port
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database.")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def fetch_data(self):
        try:
            self.cursor.execute(self.query)
            rows = self.cursor.fetchall()
            column_names = [desc[0] for desc in self.cursor.description]
            data = [dict(zip(column_names, row)) for row in rows]
            return data
        except psycopg2.Error as e:
            print(f"Error fetching data from the database: {e}")
            return None

    def produce_to_kafka(self, data):
        if data:
            try:
                for row in data:
                    self.producer.send(self.topic, value=row)
                self.producer.flush()
                print(f"Produced data to Kafka topic {self.topic}")
            except Exception as e:
                print(f"Error producing to Kafka: {e}")
        else:
            print("No data to produce.")

    def run(self):
        self.connect()
        if self.conn:
            data = self.fetch_data()
            self.produce_to_kafka(data)
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
        self.producer.close()

if __name__ == '__main__':
    # Example usage
    db_connector = DatabaseConnector(
        bootstrap_servers=['localhost:9092'],
        topic='db_topic',
        dbname='your_dbname',
        user='your_user',
        password='your_password',
        host='localhost',
        port='5432',
        query='SELECT * FROM your_table;'
    )
    db_connector.run()
