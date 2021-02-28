import json
import secrets
from flask import Flask, render_template, request

# python setup.py install
# $FLASK_APP=c:\Projects\our-vegetable-garden-project\app.py $FLASK_ENV=development flask run

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
    name = request.form["name"]
    variety = request.form["variety"]
    print(name)
    print(variety)
    return "RESPONSE_FROM_PYTHON"

APP.config["SECRET_KEY"] = secrets.token_hex(24)
if __name__ == "__main__":
    APP.run(debug=True)