# argparse_module.py
import argparse
import configparser
import os
import uuid


def validate_multiprocessing(value):
    try:
        multiprocessing_value = int(value)
        if multiprocessing_value < 0:
            raise ValueError("Multiprocessing value cannot be negative.")
        elif multiprocessing_value > os.cpu_count():
            print(
                f"Warning: Multiprocessing value is greater than the number of available CPUs. Setting it to {os.cpu_count()}.")
            return os.cpu_count()
        else:
            return multiprocessing_value
    except ValueError as e:
        raise argparse.ArgumentTypeError(str(e))


def validate_files_count(value):
    try:
        files_count_value = int(value)
        if files_count_value < 0:
            raise ValueError("Files count value cannot be negative.")
        return files_count_value
    except ValueError as e:
        raise argparse.ArgumentTypeError(str(e))


def generate_file_prefix(prefix_choice):
    if prefix_choice == "count":
        return "-count"
    elif prefix_choice == "random":
        return "-random"
    elif prefix_choice == "uuid":
        return str(uuid.uuid4())
    else:
        raise ValueError(f"Invalid choice for file_prefix: {prefix_choice}")


def parse_command_line_args():

    config = configparser.ConfigParser()
    config.read("../config/default.ini")

    # Set default values based on the configuration file
    defaults = {
        "path_to_save_files": config.get("DEFAULT", "path_to_save_files", fallback="."),
        "files_count": config.getint("DEFAULT", "files_count", fallback=0),
        "file_name": config.get("DEFAULT", "file_name", fallback="filename.txt"),
        "file_prefix": config.get("DEFAULT", "file_prefix", fallback="count"),
        "data_schema": config.get("DEFAULT", "data_schema", fallback="{}"),
        "data_lines": config.getint("DEFAULT", "data_lines", fallback=1),
        "clear_path": config.getboolean("DEFAULT", "clear_path", fallback=False),
        "multiprocessing": config.getint("DEFAULT", "multiprocessing", fallback=1),
    }

    parser = argparse.ArgumentParser(description="Process command line parameters.")

    parser.add_argument("--path_to_save_files", type=str, default=defaults["path_to_save_files"], help="Where all "
                                                                                                       "files need to "
                                                                                                       "save")
    parser.add_argument("--files_count", type=validate_files_count, default=defaults["files_count"],
                        help="How much json files to generate")
    parser.add_argument("--file_name", type=str, default=defaults["file_name"], help="File name.")
    parser.add_argument("--file_prefix", choices=["count", "random", "uuid"], default=defaults["file_prefix"],
                        help="What prefix for file name to use file needs to be generated?")
    parser.add_argument("--data_schema", type=str, default=defaults["data_schema"], help="Data schema.")
    parser.add_argument("--data_lines", type=int, default=defaults["data_lines"],
                        help="Count of lines for each file. Default, for example: 1000.")
    parser.add_argument("--clear_path", type=bool, default=defaults["clear_path"],
                        help="If this flag is on, before the script starts creating new data files, all files in "
                             "path_to_save_files that match file_name will be deleted.")
    parser.add_argument("--multiprocessing", type=validate_multiprocessing, default=defaults["multiprocessing"],
                        help="Number of processes for multiprocessing.")

    args = parser.parse_args()

    args.file_prefix = generate_file_prefix(args.file_prefix)

    return args