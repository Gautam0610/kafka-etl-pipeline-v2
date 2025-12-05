# Kafka ETL Pipeline

This project implements an ETL pipeline using Kafka for data ingestion, processing, and sinking to various data stores.

## Usage

1.  **Prerequisites:**
    *   Kafka cluster
    *   PostgreSQL database
    *   MongoDB database
    *   Elasticsearch cluster
    *   Python 3.6+

2.  **Installation:**
    ```bash
    pip install kafka-python psycopg2 pymongo elasticsearch requests
    ```

3.  **Configuration:**
    *   Update the connection parameters in the connector and sink classes with your actual database and Kafka cluster details.

4.  **Running the pipeline:**
    *   Run the connector scripts to ingest data into Kafka topics.
    *   Implement a consumer to read from the Kafka topics, apply transformations, validations, and enrichments.
    *   Run the sink scripts to load the processed data into the target data stores.

## Modules

*   **ingestion:** Contains classes for data ingestion from various sources (REST API, databases, files).
*   **processing:** Contains classes for data transformation, validation, and enrichment.
*   **sinks:** Contains classes for data sinking to various data stores (PostgreSQL, MongoDB, Elasticsearch).

## Example

To run the `RestConnector` example:

```bash
python ingestion/rest_connector.py
```

## Docker

A `Dockerfile` is provided to containerize the application. Build and run the Docker image using the following commands:

```bash
docker build -t kafka-etl .
docker run -it kafka-etl
```

**Note:** You will need to configure the Docker image with the necessary environment variables for Kafka, PostgreSQL, MongoDB, and Elasticsearch connections.
