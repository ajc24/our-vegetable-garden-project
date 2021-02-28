import os

def create_directory(path_to_dir):
    """
    Creates the specified directory
    """
    directory_path = os.getcwd() + path_to_dir
    directory_path = directory_path.replace("\\", "/")
    os.mkdir(directory_path)

def does_directory_exist(path_to_dir):
    """
    Verifies if the specified directory exists or not
    """
    directory_path = os.getcwd() + path_to_dir
    directory_path = directory_path.replace("\\", "/")
    return os.path.isdir(directory_path)

def does_file_exist(path_to_file):
    """
    Verifies if the specified file exists or not
    """
    file_path = os.getcwd() + path_to_file
    file_path = file_path.replace("\\", "/")
    return os.path.isfile(file_path)

def saveImageFile(imageFile, path_to_dir, file_name):
    """
    Saves the specified image file to the specified directory and using the specified file name
    """
    file_path = os.getcwd() + path_to_dir + "/" + file_name
    file_path = file_path.replace("\\", "/")
    imageFile.save(file_path)
