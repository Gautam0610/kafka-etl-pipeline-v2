# README

## Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Gautam0610/kafka-etl-pipeline-v2.git
    cd kafka-etl-pipeline-v2
    ```

2.  **Set up the environment:**
    *   Install Docker and Docker Compose.

3.  **Configure the environment variables:**
    *   Create a `.env` file based on the `.env.example` (if provided) and fill in the necessary values (e.g., Kafka broker address, database credentials).

4.  **Start the services:**
    ```bash
    docker-compose up -d
    ```

5.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `docker-compose.yml`: Defines services for Kafka, Zookeeper, PostgreSQL, and MongoDB.
*   `requirements.txt`: Lists Python dependencies for the project.
*   `ingestion/`: Contains modules for data ingestion.
    *   `rest_connector.py`: Placeholder for REST API data ingestion.
    *   `database_connector.py`: Placeholder for database data ingestion.
    *   `file_connector.py`: Placeholder for file data ingestion.
    *   `requirements.txt`: Lists Python dependencies for the ingestion modules.
*   `processing/`: Contains modules for data processing.
    *   `transformer.py`: Placeholder for data transformation logic.
    *   `validator.py`: Placeholder for data validation logic.
    *   `enricher.py`: Placeholder for data enrichment logic.
    *   `requirements.txt`: Lists Python dependencies for the processing modules.
*   `sinks/`: Contains modules for data sinks.
    *   `postgres_sink.py`: Placeholder for data sinking to PostgreSQL.
    *   `mongodb_sink.py`: Placeholder for data sinking to MongoDB.
    *   `elasticsearch_sink.py`: Placeholder for data sinking to Elasticsearch.
    *   `requirements.txt`: Lists Python dependencies for the sink modules.
*   `schemas/`: Contains Avro schemas.
    *   `product.avsc`: Basic schema for product data.
    *   `order.avsc`: Basic schema for order data.
