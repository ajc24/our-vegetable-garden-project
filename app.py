import json
import secrets
from flask import Flask, render_template, request
import database_manager
import file_manager
import verifications_client

# python setup.py install
# $FLASK_APP=c:\Projects\our-vegetable-garden-project\app.py $FLASK_ENV=development flask run

APP = Flask(__name__)
FILES_DIR = "/files"
IMAGE_FILE_EXTENSION = ".png"

@APP.route("/")
@APP.route("/home")
def render_home_page():
    """
    Renders the home page of the application
    """
    return render_template("HomePage.html",
        page_title = "My Home Page", )

@APP.route("/addaplant")
def render_add_a_plant_page():
    """
    Renders the add a plant page of the application
    """
    return render_template("AddAPlantPage.html",
        page_title = "Add a New Plant", )

@APP.route("/submitaddaplant", methods = ["POST"])
def submit_add_a_plant():
    """
    Submits the add a plant form to the database
    Includes all validations for user entries in the form
    """
    # Take in the plant name and validate that the name has been entered correctly
    name = request.form["name"]
    name_validation = verifications_client.verify_initial_plant_details(name)
    if name_validation["passed"] == False:
        return json.dumps(name_validation)
    # Take in the variety name and validate that the plant details are unique
    variety = request.form["variety"]
    if variety == "":
        variety = "Default"
    unique_validation = verifications_client.is_plant_unique(name, variety)
    if unique_validation["passed"] == False:
        return json.dumps(unique_validation)
    # Take in the rest of the details from the form and validate that they are correct

    # To be worked on...

    # Build the directory name needed for this new plant and the file name
    new_directory_name = name.lower().replace(" ", "-")
    new_file_name = new_directory_name + "-" + variety.lower().replace(" ", "-")
    new_image_file_name = new_file_name + IMAGE_FILE_EXTENSION
    # Take in the photo for this plant or assign None if one has not been set
    photo = None
    photo_set = False
    if "photo" in request.files:
        photo = request.files["photo"]
        photo_set = True
    # Create the directory in which to store the image file for this plant
    dir_exists = file_manager.does_directory_exist(FILES_DIR)
    if dir_exists == False:
        file_manager.create_directory(FILES_DIR)
    # Create the directory in which to store photos relating to this new plant addition
    dir_exists = file_manager.does_directory_exist(FILES_DIR + "/" + new_directory_name)
    if dir_exists == False:
        file_manager.create_directory(FILES_DIR + "/" + new_directory_name)
    # Save the profile photo for this plant in the plant directory
    if photo is not None:
        file_manager.save_image_file(photo, FILES_DIR + "/" + new_directory_name, new_image_file_name)
    # Build the new plant dictionary and save it to the database
    new_plant_json = {
        new_file_name: {
            "name": name,
            "photo_directory": new_directory_name,
            "photo_filename": new_image_file_name,
            "photo_set": photo_set,
            "variety": variety,
        }
    }
    database_manager.save_plants_dict(new_plant_json)
    return "ALL WORKING"

APP.config["SECRET_KEY"] = secrets.token_hex(24)
if __name__ == "__main__":
    APP.run(debug=True)