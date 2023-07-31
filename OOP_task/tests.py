import unittest
from CRUD.update import update_memory
from CRUD.delete import delete_component
from parts_database import parts_database

class TestUpdateFunctions(unittest.TestCase):
    def test_update_memory(self):
        name = "Memory1"
        price = 100.0
        speed = "3200 MHz"
        memory_type = "DDR4"
        cas_latency = 16

        # Call the update_memory function
        update_memory(name, price, speed, memory_type, cas_latency)

        # Assert that the memory has been updated in parts_database
        self.assertIn(name, parts_database["memory"])
        self.assertEqual(parts_database["memory"][name]["name"], name)
        self.assertEqual(parts_database["memory"][name]["price"], price)
        self.assertEqual(parts_database["memory"][name]["speed"], speed)
        self.assertEqual(parts_database["memory"][name]["type"], memory_type)
        self.assertEqual(parts_database["memory"][name]["cas_latency"], cas_latency)

    def test_delete_cpu(self):
            cpu_key = "cpu1"

            # Call the delete_component function to delete a CPU
            result = delete_component(parts_database, "cpu", cpu_key)

            # Assert that the CPU has been successfully deleted from parts_database
            self.assertTrue(result)
            self.assertNotIn(cpu_key, parts_database["cpu"])
        
        
        

if __name__ == "__main__":
    unittest.main()