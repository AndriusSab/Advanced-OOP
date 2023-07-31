import logging
from phase_one import CPU, CPUCooler, Motherboard, Memory
from database import parts_database
from CRUD.update import update_cpu, update_cpu_cooler, update_motherboard, update_memory
from CRUD.delete import delete_component
from CRUD.create import add_cpu, add_cpu_cooler, add_motherboard, add_memory


logging.basicConfig(level=logging.DEBUG, filename='oop_task.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def show_menu():
    print("===== PC Part Picker Menu =====")
    print("1. Add CPU")
    print("2. Add CPU Cooler")
    print("3. Add Motherboard")
    print("4. Add Memory")
    print("5. View All CPU's Information")
    print("6. View All CPU Coolers Information")
    print("7. View All Motherboards Information")
    print("8. View All Memories Information")
    print("9. Delete Component")
    print("10. Update Component")
    print("0. Exit")
    print("===============================")

def add_cpu_menu():
    print("==== Add CPU ====")
    name = input("Enter CPU name: ")
    price = float(input("Enter CPU price: "))
    brand = input("Enter CPU brand: ")
    speed = input("Enter CPU speed: ")
    power_usage = int(input("Enter CPU power usage: "))
    add_cpu(name, price, brand, speed, power_usage)


def add_cpu_cooler_menu():
    print("==== Add CPU Cooler ====")
    name = input("Enter CPU Cooler name: ")
    price = float(input("Enter CPU Cooler price: "))
    cooler_type = input("Enter CPU Cooler type: ")
    noise_level = float(input("Enter CPU Cooler noise level: "))
    add_cpu_cooler(name, price, cooler_type, noise_level)


def add_motherboard_menu():
    print("==== Add Motherboard ====")
    name = input("Enter Motherboard name: ")
    price = float(input("Enter Motherboard price: "))
    socket = input("Enter Motherboard socket: ")
    form_factor = input("Enter Motherboard form factor: ")
    memory_slots = int(input("Enter Motherboard memory slots: "))
    add_motherboard(name, price, socket, form_factor, memory_slots)


def add_memory_menu():
    print("==== Add Memory ====")
    name = input("Enter Memory name: ")
    price = float(input("Enter Memory price: "))
    speed = input("Enter Memory speed: ")
    memory_type = input("Enter Memory type: ")
    cas_latency = int(input("Enter Memory CAS latency: "))
    add_memory(name, price, speed, memory_type, cas_latency)



def view_cpus():
    cpus = CPU.get_all_cpus()
    for cpu in cpus:
        print(cpu.print_smth())
        print("Name:", cpu.get_name())
        print("Price:", cpu.get_price())
        print("Brand:", cpu.get_brand())
        print("Speed:", cpu.get_speed())
        print("Power Usage:", cpu.get_power_usage())
        print()

def view_cpu_coolers():
    coolers = CPUCooler.get_all_cpu_coolers()
    for cooler in coolers:
        print(cooler.print_smth())
        print("Name:", cooler.get_name())
        print("Price:", cooler.get_price())
        print("Cooler Type:", cooler.get_cooler_type())
        print("Noise Level:", cooler.get_noise_level())
        print()

def view_motherboards():
    motherboards = Motherboard.get_all_motherboards()
    for motherboard in motherboards:
        print(motherboard.print_smth())
        print("Name:", motherboard.get_name())
        print("Price:", motherboard.get_price())
        print("Socket:", motherboard.get_socket())
        print("Form Factor:", motherboard.get_form_factor())
        print("Memory Slots:", motherboard.get_memory_slots())
        print()

def view_memory_modules():
    memory_modules = Memory.get_all_memory()
    for memory in memory_modules:
        print(memory.print_smth())
        print("Name:", memory.get_name())
        print("Price:", memory.get_price())
        print("Speed:", memory.get_speed())
        print("Memory Type:", memory.get_memory_type())
        print("CAS Latency:", memory.get_cas_latency())
        print()

def update_component_menu():
    component_type = input("Enter the component type to update (cpu, cpu_cooler, motherboard, memory): ")

    if component_type == "cpu":
        name = input("Enter the CPU name: ")
        price = float(input("Enter the price: "))
        brand = input("Enter the brand: ")
        speed = input("Enter the speed: ")
        power_usage = int(input("Enter the power usage: "))
        update_cpu(name, price, brand, speed, power_usage)

    elif component_type == "cpu_cooler":
        name = input("Enter the cooler name: ")
        price = float(input("Enter the price: "))
        cooler_type = input("Enter the cooler type: ")
        noise_level = float(input("Enter the noise level: "))
        update_cpu_cooler(name, price, cooler_type, noise_level)

    elif component_type == "motherboard":
        name = input("Enter the motherboard name: ")
        price = float(input("Enter the price: "))
        socket = input("Enter the socket: ")
        form_factor = input("Enter the form factor: ")
        memory_slots = int(input("Enter the number of memory slots: "))
        update_motherboard(name, price, socket, form_factor, memory_slots)

    elif component_type == "memory":
        name = input("Enter the memory name: ")
        price = float(input("Enter the price: "))
        speed = input("Enter the speed: ")
        memory_type = input("Enter the memory type: ")
        cas_latency = int(input("Enter the CAS latency: "))
        update_memory(name, price, speed, memory_type, cas_latency)

    else:
        print("Invalid component type.")


def delete_component_menu():
    print("==== Delete Component ====")
    component_type = input("Enter component type (cpu, cpu_cooler, motherboard, memory): ")
    component_key = input("Enter component key: ")
    delete_component(parts_database, component_type, component_key)


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice (0-10): ")
        if choice == "1":
            add_cpu_menu()
        elif choice == "2":
            add_cpu_cooler_menu()
        elif choice == "3":
            add_motherboard_menu()
        elif choice == "4":
            add_memory_menu()
        elif choice == "5":
            view_cpus()
        elif choice == "6":
            view_cpu_coolers()
        elif choice == "7":
            view_motherboards()
        elif choice == "8":
            view_memory_modules()
        elif choice == "9":
            delete_component_menu()
        elif choice == "10":
            update_component_menu()
        elif choice == "0":
            print("Exiting PC Part Picker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")