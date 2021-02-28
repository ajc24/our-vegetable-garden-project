import os
from werkzeug.utils import secure_filename

DATABASE_DIR = "/database"
FILE_PLANTS_JSON = "plants.json"

def build_absolute_path(path_to_dir_or_file):
    """
    Builds the absolute path to the specified directory or file
    """
    absolute_path = os.getcwd() + path_to_dir_or_file
    absolute_path = absolute_path.replace("\\", "/")
    return absolute_path

def create_directory(path_to_dir):
    """
    Creates the specified directory
    """
    directory_path = build_absolute_path(path_to_dir)
    os.mkdir(directory_path)

def does_directory_exist(path_to_dir):
    """
    Verifies if the specified directory exists or not
    """
    directory_path = build_absolute_path(path_to_dir)
    return os.path.isdir(directory_path)

def does_file_exist(path_to_file):
    """
    Verifies if the specified file exists or not
    """
    file_path = build_absolute_path(path_to_file)
    return os.path.isfile(file_path)

def get_plants_json_file_path():
    """
    Builds the absolute path to the plants.json file in the database
    """
    return build_absolute_path(DATABASE_DIR + "/" + FILE_PLANTS_JSON)

def get_text_file(path_to_text_file):
    """
    Retrieves the text content from the specified file
    """
    with open(path_to_text_file, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def save_image_file(image_file, path_to_dir, temp_file_name):
    """
    Saves the specified image file to the specified directory and using the specified file name
    """
    final_file_name = secure_filename(temp_file_name)
    file_path = build_absolute_path(path_to_dir + "/" + final_file_name)
    image_file.save(file_path)

def save_text_file(path_to_text_file, text_content):
    """
    Saves the specified text content to the specified file at the path declared
    """
    with open(path_to_text_file, 'w') as file:
        file.write(text_content)
