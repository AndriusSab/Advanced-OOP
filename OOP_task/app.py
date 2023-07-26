from phase_one import CPU, CPUCooler, Motherboard, Memory
from CRUD.delete import delete_component
from CRUD.update import update_cpu, update_cooler, update_motherboard, update_memory

def display_menu():
    print("Welcome to PC PART PICKER!")
    print("1. View CPUs")
    print("2. View CPU Coolers")
    print("3. View Motherboards")
    print("4. View Memory Modules")
    print("5. Update Component")
    print("6. Delete Component")
    print("7. Exit")

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

def update_component():
    component_type = input("Enter the component type to update (cpu, cpu_cooler, motherboard, memory): ")
    component_key = input("Enter the component key to update: ")

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
        update_cooler(name, price, cooler_type, noise_level)

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

def delete_component():
    component_type = input("Enter the component type to delete (cpu, cpu_cooler, motherboard, memory): ")
    component_key = input("Enter the component key to delete: ")
    delete_component(parts_database, component_type, component_key)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            view_cpus()
        elif choice == "2":
            view_cpu_coolers()
        elif choice == "3":
            view_motherboards()
        elif choice == "4":
            view_memory_modules()
        elif choice == "5":
            update_component()
        elif choice == "6":
            delete_component()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()