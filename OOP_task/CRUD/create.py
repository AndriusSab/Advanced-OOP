
from  database import parts_database
import logging

import logging

def generate_cpu_name(cpu_count):
    return f"cpu{cpu_count}"

def add_cpu(name, price, brand, speed, power_usage):
    try:
        cpu_data = {
            "name": name,
            "price": price,
            "brand": brand,
            "speed": speed,
            "power_usage": power_usage
        }
        parts_database["cpu"][name] = cpu_data
        logging.info(f"CPU '{name}' has been added to the database.")
    except Exception as e:
        logging.exception(f"Error occurred while adding CPU '{name}' to the database.")
        raise e
    
def add_cpu_cooler(name, price, cooler_type, noise_level):
    try:
        cooler_data = {
            "name": name,
            "price": price,
            "cooler_type": cooler_type,
            "noise_level": noise_level
        }
        parts_database["cpu_cooler"][name] = cooler_data
        logging.info(f"Cooler '{name}' has been added to the database.")
    except Exception as e:
        logging.exception(f"Error occurred while adding Cooler '{name}' to the database.")
        raise e


def add_motherboard(name, price, socket, form_factor, memory_slots):
    try:
        motherboard_data = {
            "name": name,
            "price": price,
            "socket": socket,
            "form_factor": form_factor,
            "memory_slots": memory_slots
        }
        parts_database["motherboard"][name] = motherboard_data
        logging.info(f"Motherboard '{name}' has been added to the database.")
    except Exception as e:
        logging.exception(f"Error occurred while adding Motherboard '{name}' to the database.")
        raise e


def add_memory(name, price, speed, memory_type, cas_latency):
    try:
        memory_data = {
            "name": name,
            "price": price,
            "speed": speed,
            "memory_type": memory_type,
            "cas_latency": cas_latency
        }
        parts_database["memory"][name] = memory_data
        logging.info(f"Memory '{name}' has been added to the database.")
    except Exception as e:
        logging.exception(f"Error occurred while adding Memory '{name}' to the database.")
        raise e