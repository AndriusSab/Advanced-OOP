import parts_database
from typing import Dict
import logger


def delete_component(database, component_type, component_key):
 
    try:
        if component_type in database and component_key in database[component_type]:
            removed_component = database[component_type].pop(component_key)
            logging.info(f"Successfully removed {component_type}: {removed_component['name']}")
            return True
        else:
            logging.warning(f"{component_type} with key {component_key} not found in the database.")
            return False
    except Exception as e:
        logging.exception(f"Error occurred while deleting {component_type} with key {component_key}.")
        raise e
