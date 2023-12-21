import os
import uuid
import logging


def output_filenames_list(file_name, file_prefix=None, file_counter=1):
    files_list = []
    for i in range(1, file_counter + 1):
        if file_prefix is None:
            files_list.append(f"{file_name}.json")
        elif file_prefix == "-random":
            uuid_str = str(uuid.uuid4())
            files_list.append(f"{file_name}_{uuid_str}.json")
        else:
            files_list.append(f"{file_name}_{i}.json")
    return files_list


def prepare_directory(path_to_save_files, file_name, clear_path=False):
    os.chdir(path_to_save_files)
    logging.info(f"Output files are stored in: {os.getcwd()}")

    if clear_path:
        for file in os.listdir(os.getcwd()):
            if file.startswith(file_name):
                try:
                    os.remove(file)
                    logging.info(f"File '{file}' deleted successfully.")
                except Exception as e:
                    logging.warning(f"File '{file}' does not exist: {e}")
