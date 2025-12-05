import json

class Transformer:
    def __init__(self, transformation_function=None):
        self.transformation_function = transformation_function or self.default_transformation

    def default_transformation(self, data):
        # Default transformation: convert data to uppercase
        if isinstance(data, str):
            return data.upper()
        elif isinstance(data, dict):
            return {k: self.default_transformation(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.default_transformation(item) for item in data]
        else:
            return data  # Return unchanged if not string, dict, or list

    def transform(self, data):
        return self.transformation_function(data)

if __name__ == '__main__':
    # Example usage
    transformer = Transformer()
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    transformed_data = transformer.transform(data)
    print(f"Transformed data: {transformed_data}")

    # Example with a custom transformation function
    def custom_transformation(data):
        if isinstance(data, dict):
            return {k: v * 2 if isinstance(v, (int, float)) else v for k, v in data.items()}
        return data

    custom_transformer = Transformer(transformation_function=custom_transformation)
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    transformed_data = custom_transformer.transform(data)
    print(f"Transformed data with custom function: {transformed_data}")