import json
import secrets
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import file_manager

# python setup.py install
# $FLASK_APP=c:\Projects\our-vegetable-garden-project\app.py $FLASK_ENV=development flask run

FILES_DIR = "/files"

APP = Flask(__name__)

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
    return render_template("AddPlantPage.html",
        page_title = "Add a New Plant", )

@APP.route("/submitaddaplant", methods = ["POST"])
def submit_add_a_plant():
    # Take in the plant name and create the file directory name from it
    name = request.form["name"]
    directory_name = name.lower().replace(" ", "-")
    # Take in the variety name and create the file image name from it
    variety = request.form["variety"]
    if variety == "":
        variety = "Default"
    temp_file_name = name.lower().replace(" ", "-") + "-" + variety.lower().replace(" ", "-") + ".png"
    # Take in the photo for this plant
    photo = request.files["photo"]
    # Debugging output
    print("NAME: " + name)
    print("DIR NAME: " + directory_name)
    print("FILE NAME: " + temp_file_name)
    print("VARIETY: " + variety)
    # Create the directory in which to store the image file for this plant
    dir_exists = file_manager.does_directory_exist(FILES_DIR)
    if dir_exists == False:
        print("***** CREATE FILES DIRECTORY")
        file_manager.create_directory(FILES_DIR)
    dir_exists = file_manager.does_directory_exist(FILES_DIR + "/" + directory_name)
    if dir_exists == False:
        print("***** CREATE IMAGE FILE DIRECTORY")
        file_manager.create_directory(FILES_DIR + "/" + directory_name)
    final_file_name = secure_filename(temp_file_name)
    file_exists = file_manager.does_file_exist(FILES_DIR + "/" + directory_name + "/" + final_file_name)
    if file_exists == False:
        print("***** CREATE NEW IMAGE FILE")
        file_manager.saveImageFile(photo, FILES_DIR + "/" + directory_name, final_file_name)
    print("***** DONE")
    return "RESPONSE_FROM_PYTHON"

APP.config["SECRET_KEY"] = secrets.token_hex(24)
if __name__ == "__main__":
    APP.run(debug=True)