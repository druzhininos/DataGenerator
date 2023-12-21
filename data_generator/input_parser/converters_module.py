import ast
import json
import sys
import os
import logging


def data_schema_str_to_dict(data_schema_str):
    try:
        # Use ast.literal_eval to safely evaluate the string as a literal Python expression
        data_schema_dict = ast.literal_eval(data_schema_str)
        if not isinstance(data_schema_dict, dict):
            logging.error(f"Invalid data schema format: Not a dictionary")
            sys.exit(1)
        return data_schema_dict
    except (SyntaxError, ValueError) as e:
        logging.error(f"Error parsing data schema: {e}")
        sys.exit(1)


def write_dict_to_file(file_name, generator, lines_count):
    try:
        with open(file_name, 'w') as file:
            for _ in range(lines_count):
                json.dump(generator.generate_instance(), file)
                file.write('\n')
        logging.info(f"Data written to '{file_name}' successfully.")
    except Exception as e:
        logging.error(f"Error writing data to file '{file_name}': {e}")
        sys.exit(1)
