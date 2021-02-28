import database_manager

def is_plant_unique(plant_name, plant_variety):
    """
    Verifies that the plant details being registered are unique
    """
    validation = {
      "passed": True,
      "errors": [],
    }
    base_key = plant_name.lower().replace(" ", "-") + "-" + plant_variety.lower().replace(" ", "-")
    plants_dict = database_manager.get_plants_dict()
    if base_key in plants_dict:
        validation["passed"] = False
        validation["errors"].append("The plant details you have entered (name and variety) already exist in our system.")
    return validation

def verify_initial_plant_details(plant_name):
    """
    Verifies that the plants name is a valid input
    """
    validation = {
      "passed": True,
      "errors": [],
    }
    if plant_name == "":
        validation["passed"] = False
        validation["errors"].append("You did not enter a name for your new plant.")
    return validation
