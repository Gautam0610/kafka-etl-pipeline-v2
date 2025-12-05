from pymongo import MongoClient

class MongoDBSink:
    def __init__(self, host, port, db_name, collection_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None

    def connect(self):
        try:
            self.client = MongoClient(host=self.host, port=self.port)
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            print("Connected to MongoDB.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return False
        return True

    def sink(self, data):
        if not self.collection:
            print("Not connected to MongoDB.")
            return False

        try:
            if isinstance(data, list):
                self.collection.insert_many(data)
            else:
                self.collection.insert_one(data)
            print("Data inserted into MongoDB.")
        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")
            return False
        return True

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

if __name__ == '__main__':
    # Example Usage
    mongodb_sink = MongoDBSink(
        host='localhost',
        port=27017,
        db_name='your_db',
        collection_name='your_collection'
    )

    if mongodb_sink.connect():
        data = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
        mongodb_sink.sink(data)
        mongodb_sink.close()
