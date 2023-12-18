from argparse_module import parse_command_line_args


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    command_line_args = parse_command_line_args()

    path_to_save_files = command_line_args.path_to_save_files
    files_count = command_line_args.files_count
    file_name = command_line_args.file_name
    file_prefix = command_line_args.file_prefix
    data_schema = command_line_args.data_schema
    data_lines = command_line_args.data_lines
    clear_path = command_line_args.clear_path
    multiprocessing_enabled = command_line_args.multiprocessing

    # Use the parameters in your code as needed
    print("Path to save files:", path_to_save_files)
    print("Files count:", files_count)
    print("File name:", file_name)
    print("File prefix:", file_prefix)
    print("Data schema:", data_schema)
    print("Data lines:", data_lines)
    print("Clear path:", clear_path)
    print("Multiprocessing enabled:", multiprocessing_enabled)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
