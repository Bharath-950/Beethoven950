from .validator import validate_data
def process_data(data):
    if(not validate_data(data)):
        return f"Processes Data:{data}"
    return "Invalid Data"