import random
import logging
import time
import uuid


class Generator:
    def __init__(self, data_schema):
        self.data_schema = data_schema

    def generate_instance(self):
        instance = {}
        for key, value in self.data_schema.items():
            instance[key] = self.parse_and_generate_value(value, key)
        return instance

    def parse_and_generate_value(self, value, key):
        parts = value.split(":")
        data_type = parts[0].strip()

        if data_type == "timestamp":
            if parts[1]:
                logging.warning(f"Timestamp does not support any values in schema: Invalid value '{parts[1]}'")
            return int(time.time())
        elif data_type == "str":
            return self.generate_string_value(parts[1].strip())
        elif data_type == "int":
            return self.generate_int_value(parts[1].strip())
        else:
            logging.error(f"Unsupported data type: {data_type}")
            return None


    def generate_string_value(self, value):
        if value == "rand":
            return str(uuid.uuid4())
        elif value.startswith("[") and value.endswith("]"):
            options = [option.strip() for option in value[1:-1].split(',')]
            return random.choice(options)
        elif not value:
            return ""
        else:
            return value

    def generate_int_value(self, value):
        if value == "rand":
            return random.randint(0, 10000)
        elif value.startswith("[") and value.endswith("]"):
            options = [int(option.strip()) for option in value[1:-1].split(',')]
            return random.choice(options)
        elif value.startswith("rand(") and value.endswith(")"):
            range_values = value[5:-1].split(',')
            min_value, max_value = int(range_values[0]), int(range_values[1])
            return random.randint(min_value, max_value)
        elif not value:
            return None
        else:
            logging.error(f"Error in schema: Invalid value '{value}' for int type.")
            return None

