class Validator:
    def __init__(self, schema=None):
        self.schema = schema

    def validate(self, data):
        if self.schema is None:
            # If no schema is provided, consider the data valid
            return True, "No schema provided, data considered valid."

        try:
            # For simplicity, assuming schema is a dict with required keys
            if not isinstance(data, dict):
                return False, "Data is not a dictionary."

            for key in self.schema.get("required", []):
                if key not in data:
                    return False, f"Missing required key: {key}"

            return True, "Data is valid."

        except Exception as e:
            return False, f"Validation error: {e}"

if __name__ == '__main__':
    # Example usage
    schema = {"required": ["name", "age"]}
    validator = Validator(schema=schema)

    data1 = {"name": "John", "age": 30}
    is_valid1, message1 = validator.validate(data1)
    print(f"Data 1 is valid: {is_valid1}, Message: {message1}")

    data2 = {"name": "John"}
    is_valid2, message2 = validator.validate(data2)
    print(f"Data 2 is valid: {is_valid2}, Message: {message2}")
