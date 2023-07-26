from  parts_database import parts_database
import logging

logging.basicConfig(level=logging.DEBUG,filename='oop_task.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')




def update_cpu(name, price, brand, speed, power_usage):
    try:
        cpu_data = {
            "name": name,
            "price": price,
            "brand": brand,
            "speed": speed,
            "power_usage": power_usage
        }
        parts_database["cpu"][name] = cpu_data
        logging.info(f"CPU '{name}' has been updated in the database.")
    except Exception as e:
        logging.exception(f"Error occurred while updating CPU '{name}' in the database.")
        raise e

    
def update_cooler(name, price, cooler_type, noise_level):
    try:
        if name in parts_database.get("cpu_cooler", {}):
            cooler_data = {
                "name": name,
                "price": price,
                "cooler_type": cooler_type,
                "noise_level": noise_level
            }
            parts_database["cpu_cooler"][name] = cooler_data
            logging.info(f"Cooler '{name}' has been updated in the database.")
        else:
            logging.warning(f"Cooler '{name}' not found in the database.")
    except Exception as e:
        logging.exception(f"Error occurred while updating Cooler '{name}' in the database.")
        raise e
    
    
def update_motherboard(name: str, price: float, speed: str, memory_type: str, memory_slots: int):
    try:
        if name in parts_database.get("motherboard", {}):
            motherboard_data = {
                "name": name,
                "price": price,
                "speed": speed,
                "memory_type": memory_type,
                "memory_slots": memory_slots,
            }
            parts_database["motherboard"][name] = motherboard_data
            logging.info(f"Motherboard '{name}' has been updated in the database.")
        else:
            logging.warning(f"Motherboard '{name}' not found in the database.")
    except Exception as e:
        logging.exception(f"Error occurred while updating Motherboard '{name}' in the database.")
        raise e
    
def update_memory(name: str, price: float, speed: str, memory_type: str, cas_latency: int):
    try:
        if name in parts_database.get("memory", {}):
            memory_data = {
                "name": name,
                "price": price,
                "speed": speed,
                "type": memory_type,
                "cas_latency": cas_latency,
            }
            parts_database["memory"][name] = memory_data
            logging.info(f"Memory '{name}' has been updated in the database.")
        else:
            logging.warning(f"Memory '{name}' not found in the database.")
    except Exception as e:
        logging.exception(f"Error occurred while updating Memory '{name}' in the database.")
        raise e
        


    