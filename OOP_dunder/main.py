# class Product:
#     def __init__(self, name: str, price: float) -> None:
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"Prdoduct {self.name}, Price:{self.price}"

#     def __repr__(self) -> str:
#         return f"Prdoduct {self.name}, Price:{self.price}"


# product = Product("Kebabas", 6)

# print(str(product))
# print(repr(product))


# class MyQueue:
#     def __init__(self, items: list):
#         self.items = items

#     def __bool__(self) -> bool:
#         return bool(self.items)

#     def __repr__(self) -> str:
#         return f"MyQueue({self.items})"

#     def __len__(self) -> int:
#         return len(self.items)


# myqueue = MyQueue(["hi", "bye", "world"])
# print(bool(myqueue))
# print(myqueue)
# print(len(myqueue))


# Create three different task with real world scenario what would include all magic methods we covered today and plus 3 others from the provided list.


class FishingEquipment:
    """FishingEquipment class provides name and quantity of items of different fishing equipment"""

    def __init__(
        self, brand_name: list, quantity_stock: float, quantity_order, type: str
    ) -> None:
        self.brand_name = brand_name
        self.quantity_stock = quantity_stock
        self.quantity_order = quantity_order
        self.type = type

    def __bool__(self) -> bool:
        if self.type == "saltwater":
            return True
        return False

    def __repr__(self) -> str:
        return f"Fishing equipment name({self.brand_name}, stock quantity: {self.quantity_stock}, ordered quantity {self.quantity_order} type{self.type}, )"

    def __len__(self) -> int:
        return len(self.brand_name)

    def __name__(self) -> str:
        return "Fishing Equipment"

    def __doc__(self) -> str:
        return "FishingEquipment class provides name and quantity of items of different fishing equipment"

    def __getitem__(self, index) -> str:
        if index >= 0:
            return self.brand_name[index]
        return ValueError

    def __contains__(self, item) -> bool:
        return item in self.brand_name


fishingeq = FishingEquipment(
    brand_name=["Shimano", "Daiwa", "Salmo"],
    quantity_stock=100,
    quantity_order=10,
    type="saltwater",
)

print(bool(fishingeq))
print(fishingeq)
print(len(fishingeq))
print(fishingeq.__name__())
print(fishingeq.__doc__())
print(fishingeq[-5])
print("Shimano" in fishingeq)
