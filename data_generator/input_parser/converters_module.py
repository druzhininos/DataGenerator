import ast


def data_schema_str_to_dict(data_schema_str):
    try:
        # Use ast.literal_eval to safely evaluate the string as a literal Python expression
        data_schema_dict = ast.literal_eval(data_schema_str)
        if not isinstance(data_schema_dict, dict):
            raise ValueError("Invalid data schema format: Not a dictionary")
        return data_schema_dict
    except (SyntaxError, ValueError) as e:
        print(f"Error parsing data schema: {e}")
        return None
