class Enricher:
    def __init__(self, enrichment_data=None):
        self.enrichment_data = enrichment_data or {}

    def enrich(self, data):
        if not isinstance(data, dict):
            return data  # Can only enrich dictionaries

        enriched_data = data.copy()
        for key, value in self.enrichment_data.items():
            enriched_data[key] = value

        return enriched_data

if __name__ == '__main__':
    # Example Usage
    enrichment_data = {"country": "USA", "data_source": "local"}
    enricher = Enricher(enrichment_data=enrichment_data)

    data = {"name": "John", "age": 30}
    enriched_data = enricher.enrich(data)
    print(f"Enriched Data: {enriched_data}")
