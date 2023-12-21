
from argparse_module import parse_command_line_args
from data_generator.input_parser import generator_module, converters_module
import os_module
import logging
import multiprocessing

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    command_line_args = parse_command_line_args()

    path_to_save_files = command_line_args.path_to_save_files
    files_count = int(command_line_args.files_count)
    file_name = command_line_args.file_name
    file_prefix = command_line_args.file_prefix
    data_schema = converters_module.data_schema_str_to_dict(command_line_args.data_schema)
    data_lines = int(command_line_args.data_lines)
    clear_path = bool(command_line_args.clear_path)
    multiprocessing_enabled = int(command_line_args.multiprocessing)

    # Use the parameters in your code as needed
    logging.debug(f"Path to save files: {path_to_save_files}")
    logging.debug(f"Files count: {files_count}")
    logging.debug(f"File name: {file_name}")
    logging.debug(f"File prefix: {file_prefix}")
    logging.debug(f"Data schema: {data_schema}")
    logging.debug(f"Data lines: {data_lines}")
    logging.debug(f"Clear path: {clear_path}")
    logging.debug(f"Multiprocessing enabled: {multiprocessing_enabled}")

    # Parsing data schema, storing as a Dict
    generator = generator_module.Generator(data_schema)
    # Showing on screen
    if files_count == 0:
        for _ in range(data_lines):
            instance = generator.generate_instance()
            print(instance)
    # or writing in a file
    else:
        files_list = os_module.output_filenames_list(file_name, file_prefix, files_count)
        os_module.prepare_directory(path_to_save_files, file_name, clear_path)
        with multiprocessing.Pool(processes=multiprocessing_enabled) as pool:
            pool.starmap(converters_module.write_dict_to_file, [(file, generator, data_lines) for file in files_list])