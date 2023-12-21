from data_generator.input_parser.converters_module import data_schema_str_to_dict


def test_data_schema_str_to_dict():
    data_schema = '{\'date\': \'timestamp:\', \'fname\': \'str:Hollys\', \'name\': \'str:rand\', ' \
                  '\'type\': "str:[\'client\', \'partner\', \'government\']", \'age\': \'int:rand(1, 90)\'}'

    # Call the parse_data_schema function
    parsed_data = data_schema_str_to_dict(data_schema)

    # Assertions to check if the parsing is correct
    assert "date" in parsed_data
    assert "name" in parsed_data
    assert "type" in parsed_data
    assert "age" in parsed_data

    assert parsed_data["date"] == "timestamp:"
    assert parsed_data["name"] == "str:rand"
    assert parsed_data["type"] == "str:['client', 'partner', 'government']"
    assert parsed_data["age"] == "int:rand(1, 90)"
