from  database import parts_database
import logging

logging.basicConfig(level=logging.DEBUG,filename='oop_task.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')




def update_cpu(name, price, brand, speed, power_usage):
    try:
        if name not in parts_database["cpu"]:
            raise ValueError(f"CPU with name '{name}' does not exist in the database.")
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

    
def update_cpu_cooler(name, price, cooler_type, noise_level):
    try:
        if name not in parts_database["cpu_cooler"]:
            raise ValueError(f"Cooler with name '{name}' does not exist in the database.")
        cooler_data = {
            "name": name,
            "price": price,
            "cooler_type": cooler_type,
            "noise_level": noise_level
        }
        parts_database["cpu_cooler"][name] = cooler_data
        logging.info(f"Cooler '{name}' has been updated in the database.")
    except Exception as e:
        logging.exception(f"Error occurred while updating CPU Cooler '{name}' in the database.")
        raise e
    
    
def update_motherboard(name, price, socket, form_factor, memory_slots):
    try:
        if name not in parts_database["motherboard"]:
            raise ValueError(f"Motherboard with name '{name}' does not exist in the database.")
        motherboard_data = {
            "name": name,
            "price": price,
            "socket": socket,
            "form_factor": form_factor,
            "memory_slots": memory_slots
        }
        parts_database["motherboard"][name] = motherboard_data
        logging.info(f"Motherboard '{name}' has been updated in the database.")
    except Exception as e:
        logging.exception(f"Error occurred while updating Motherboard '{name}' in the database.")
        raise e
    
def update_memory(name, price, speed, memory_type, cas_latency):
    try:
        if name not in parts_database["memory"]:
            raise ValueError(f"Memory with name '{name}' does not exist in the database.")
        memory_data = {
            "name": name,
            "price": price,
            "speed": speed,
            "type": memory_type,
            "cas_latency": cas_latency
        }
        parts_database["memory"][name] = memory_data
        logging.info(f"Memory '{name}' has been updated in the database.")
    except Exception as e:
        logging.exception(f"Error occurred while updating Memory '{name}' in the database.")
        raise e
        


    