
import requests
from kafka import KafkaProducer
import json

class RestConnector:
    def __init__(self, bootstrap_servers, topic, url):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.url = url
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {self.url}: {e}")
            return None

    def produce_to_kafka(self, data):
        if data:
            try:
                self.producer.send(self.topic, value=data)
                self.producer.flush()
                print(f"Produced data to Kafka topic {self.topic}")
            except Exception as e:
                print(f"Error producing to Kafka: {e}")
        else:
            print("No data to produce.")

    def run(self):
        data = self.fetch_data()
        self.produce_to_kafka(data)

    def close(self):
        self.producer.close()

if __name__ == '__main__':
    # Example usage
    rest_connector = RestConnector(
        bootstrap_servers=['localhost:9092'],
        topic='rest_topic',
        url='https://jsonplaceholder.typicode.com/todos/1'
    )
    rest_connector.run()
    rest_connector.close()
