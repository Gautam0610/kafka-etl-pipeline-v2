import json
from kafka import KafkaProducer

class FileConnector:
    def __init__(self, bootstrap_servers, topic, file_path):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.file_path = file_path
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def read_file(self):
        try:
            with open(self.file_path, 'r') as f:
                # Assuming each line in the file is a JSON object
                data = [json.loads(line) for line in f]
            return data
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")
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
        data = self.read_file()
        self.produce_to_kafka(data)
        self.close()

    def close(self):
        self.producer.close()

if __name__ == '__main__':
    # Example usage
    file_connector = FileConnector(
        bootstrap_servers=['localhost:9092'],
        topic='file_topic',
        file_path='data.json'  # Replace with your file path
    )
    # Create a dummy data.json file for testing
    with open('data.json', 'w') as f:
        json.dump([{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}], f)

    file_connector.run()
