from elasticsearch import Elasticsearch

class ElasticsearchSink:
    def __init__(self, host, port, index_name):
        self.host = host
        self.port = port
        self.index_name = index_name
        self.es_client = None

    def connect(self):
        try:
            self.es_client = Elasticsearch([{'host': self.host, 'port': self.port}])
            if self.es_client.ping():
                print("Connected to Elasticsearch.")
                return True
            else:
                print("Failed to connect to Elasticsearch.")
                return False
        except Exception as e:
            print(f"Error connecting to Elasticsearch: {e}")
            return False

    def sink(self, data):
        if not self.es_client:
            print("Not connected to Elasticsearch.")
            return False

        try:
            if isinstance(data, list):
                for item in data:
                    self.es_client.index(index=self.index_name, document=item)
            else:
                self.es_client.index(index=self.index_name, document=data)
            print("Data indexed in Elasticsearch.")
        except Exception as e:
            print(f"Error indexing data in Elasticsearch: {e}")
            return False
        return True

    def close(self):
        # Elasticsearch client does not need to be closed explicitly.
        print("Elasticsearch connection closed.")

if __name__ == '__main__':
    # Example Usage
    elasticsearch_sink = ElasticsearchSink(
        host='localhost',
        port=9200,
        index_name='your_index'
    )

    if elasticsearch_sink.connect():
        data = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
        elasticsearch_sink.sink(data)
        elasticsearch_sink.close()
