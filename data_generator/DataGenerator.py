import json
import random
import time
import logging

def generate_data(schema, num_records):
    data = []
    for _ in range(num_records):
        record = {}
        for key, value in schema.items():
            data_type, *args = value.split(':')
            if data_type == 'str':
                if args and args[0] == 'rand':
                    record[key] = str(uuid.uuid4())
                elif args and args[0].startswith('[') and args[0].endswith(']'):
                    options = eval(args[0])
                    record[key] = random.choice(options)
                elif args and args[0].startswith('rand(') and args[0].endswith(')'):
                    range_args = eval(args[0][5:-1])
                    record[key] = random.randint(*range_args)
                elif args and args[0]:
                    logging.error(f"Error: Invalid value {args[0]} for key {key}")
                else:
                    record[key] = args[0] if args else ''
            elif data_type == 'int':
                if args and args[0] == 'rand':
                    record[key] = random.randint(0, 10000)
                elif args and args[0].startswith('[') and args[0].endswith(']'):
                    options = eval(args[0])
                    record[key] = random.choice(options)
                elif args and args[0].startswith('rand(') and args[0].endswith(')'):
                    logging.error(f"Error: Invalid value {args[0]} for key {key}")
                elif args and args[0]:
                    record[key] = int(args[0])
                else:
                    record[key] = None
            elif data_type == 'timestamp':
                logging.warning(f"Ignoring values after ':' for timestamp type in key {key}")
                record[key] = int(time.time())
        data.append(record)
    return data

if __name__ == "__main__":
    schema_str = input("Enter the input data schema in JSON format: ")
    num_records = int(input("Enter the number of records to generate: "))

    try:
        schema = json.loads(schema_str)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format for input schema.")
        exit(1)

    generated_data = generate_data(schema, num_records)
    print(json.dumps(generated_data, indent=2))
