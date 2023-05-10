# Google is launching a network of autonomous pizza delivery drones and
# wants you to create a flexible rewards system (Pizza Points™) that can be tweaked in the future. 
# The rules are simple: if a customer has made at least N orders of at least Y price, 
# they get a FREE pizza! Create a function that takes a dictionary of customers,
# a minimum number of orders and a minimum order price. 
# Return a list of customers that are eligible for a free pizza.

class PizzaPoints:
    def __init__(self, customers:dict, min_orders:int, min_ord_price:float ):
        
        self.customers = customers
        self.min_orders = min_orders
        self.min_ord_price = min_ord_price    
        
        
    def check_for_eligible (self) ->list:
        free_pizza_eaters =[]
        for self.customer, orders in  self.customers.items():
            if len(orders) >= self.min_orders:
                total_spent_money = sum(orders)
                if total_spent_money >= self.min_orders * self.min_ord_price:
                    free_pizza_eaters.append(self.customer)
    
        return free_pizza_eaters
        
if __name__=="__main__":
        
 customers = {
            "Andrius":[5, 8, 10, 15],
            "Stasys":[8, 12, 45],
            "Darius":[60, 50, 40]
            }
 free_pizza = PizzaPoints(customer=customers, 2, 30)
 
 
 
print(free_pizza.check_for_eligible())
 