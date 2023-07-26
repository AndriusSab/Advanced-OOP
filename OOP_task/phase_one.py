# Phase 1: 
# Create a class that would represent pc parts. It should contain basic methods to retreive items name, price, colour (if applicable).
# PC part list can be found here: https://pcpartpicker.com/list/
# The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)
# At this stage, dictionary data structures can work as Database. OOP abstraction, inheritance and encapsulation must be presented in a code base. 
# Unit tests must be written for the methods.


"""PC PART PICKER """
from  parts_database import parts_database
from typing import Dict
from abc import ABC, abstractmethod
import logger


class PCPARTS(ABC):
    def __init__(self, name:str, price: float):
        self.name = name
        self.price = price
    
    def get_name(self) -> str:
        return self.name
    
    def  get_price(self) -> float:
        return self.price
    
    @abstractmethod
    def print_smth(self):
        pass
    

class CPU(PCPARTS):
    def __init__(self, name: str, price:float, brand:str, speed:float, power_usage:int):
        super().__init__(name, price)
        self.brand = brand
        self.speed = speed
        self.power_usage = power_usage
        
    @staticmethod
    def get_all_cpus():
        try:
            cpu_items = parts_database.get("cpu", {})
            cpu_objects = []
            for item_key, item_data in cpu_items.items():
                cpu = CPU(item_data["name"], item_data["price"], item_data["brand"], item_data["speed"], item_data["power_usage"])
                cpu_objects.append(cpu)
            return cpu_objects
        except Exception as e:
            raise e 
 
    def get_brand(self):
        return self.brand
    
    def get_speed(self):
        return self.speed
    
    def get_power_usage(self):
        return self.power_usage
    
    
    def print_smth(self):
        return f"CPU Information"
    
    

class CPUCooler(PCPARTS):
    def __init__(self, name:str, price:float, cooler_type:str, noise_level:float):
        super().__init__(name, price)
        self.cooler_type = cooler_type
        self.noise_level = noise_level
    
    def get_all_cpu_coolers():
        try:
            cooler_items = parts_database.get("cpu_cooler", {})
            cooler_objects = []
            for item_key, item_data in cooler_items.items():
                cooler = CPUCooler(item_data["name"], item_data["price"], item_data["cooler_type"], item_data["noise_level"])
                cooler_objects.append(cooler)
            return cooler_objects
        except Exception as e:
            raise e    
    
    def get_cooler_type(self):
        return self.cooler_type

    def get_noise_level(self):
        return self.noise_level
    
    def print_smth(self):
        return f"CPUCooler Information"
    
class Motherboard(PCPARTS):
    def __init__(self, name: str, price: float, socket: str, form_factor: str, memory_slots: int):
        super().__init__(name, price)
        self.socket = socket
        self.form_factor = form_factor
        self.memory_slots = memory_slots
    
    
    def get_all_motherboards():
        try:
            motherboard_items = parts_database.get("motherboard", {})
            motherboard_objects = []
            for item_key, item_data in motherboard_items.items():
                motherboard = Motherboard(item_data["name"], item_data["price"], item_data["socket"], item_data["form_factor"],item_data["memory_slots"] )
                motherboard_objects.append(motherboard)
            return motherboard_objects
        except Exception as e:
            raise e    
    
    
    def get_socket(self) -> str:
        return self.socket
    
    def get_form_factor(self) -> str:
        return self.form_factor
    
    def get_memory_slots(self) -> int:
        return self.memory_slots
    
    def print_smth(self):
        return f"Motherboards Information"

class Memory(PCPARTS):
    def __init__(self, name: str, price: float, speed: str, memory_type: str, cas_latency: int):
        super().__init__(name, price)
        self.speed = speed
        self.memory_type = memory_type
        self.cas_latency = cas_latency
        
    def get_all_memory():
        try:
            memory_items = parts_database.get("memory", {})
            memory_objects = []
            for item_key, item_data in memory_items.items():
                memory = Memory(item_data["name"], item_data["price"], item_data["speed"], item_data["type"],item_data["cas_latency"] )
                memory_objects.append(memory)
            return memory_objects
        except Exception as e:
            raise e           
        
    
    def get_speed(self) -> str:
        return self.speed
    
    def get_memory_type(self) -> str:
        return self.memory_type
    
    def get_cas_latency(self) -> int:
        return self.cas_latency
    
    def print_smth(self):
        return f"Memories Information"



