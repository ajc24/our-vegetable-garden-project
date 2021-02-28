import json
import file_manager

def get_plants_dict():
    """
    Retrieves the plants data from the file database
    """
    json_data_file_path = file_manager.get_plants_json_file_path()
    json_data = file_manager.get_text_file(json_data_file_path)
    return json.loads(json_data)

def save_plants_dict(json_data_append):
    """
    Saves the new plants json data to the database
    """
    # Merge the new data with the existing data
    existing_dict = get_plants_dict()
    joined_dict = existing_dict | json_data_append
    # Save the file to the database
    json_data_file_path = file_manager.get_plants_json_file_path()
    file_manager.save_text_file(json_data_file_path, json.dumps(joined_dict))
