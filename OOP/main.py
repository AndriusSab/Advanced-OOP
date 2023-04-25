# You have been asked to create a simple inventory management system for a small retail store.
#  You need to define a Product class using the dataclass module that represents a product in the store.
# Each Product should have a unique ID, a name, a description, a price, and a quantity in  stock.
# You also need to You have been asked to create a simple inventory management system for a small retail store.
# You need to define a Product class using the dataclass module that represents a product in the store.
# Each Product should have a unique ID, a name, a description, a price, and a quantity in  stock.
# You also need to implement a method calculate_total_cost that calculates the total cost of a given number of items of the product,
# taking into account any discounts that may apply.implement a method calculate_total_cost that calculates the total cost of a given number of items of the product,
# taking into account any discounts that may apply.

from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    quantity: int

    def calculate_total_cost(self, number_of_item: int = None) -> float:
        if number_of_item is None:
            return self.price * self.quantity
        else:
            return self.price * number_of_item


product = Product(id=1, name="Morka", description="Plautos", price=2.00, quantity=10)

print(product.calculate_total_cost())
print(product.calculate_total_cost(10))


# You need to create a program to manage a list of books in a library. Each book has a title, an author, a publication year, and an ISBN.
# You need to define a Book class using the dataclass module that contains attributes for these properties. 
# You also need to implement a Library class that manages a list of books. The Library class should allow you to add and remove books from the library,
#  search for books by title or author, and display the list of books currently in the library.

from dataclasses import dataclass


@dataclass
class Book:
    
    title :str
    author: str
    public_year: int
    ISBN = int

@dataclass
class Library:
    
    self.books.List[Book] = []
    
    def add_book(self, book: Book) ->None:
        return self.books.append(book)  
    
    def remove_book(self, book:):
        return self.books.remove(book)
    
    def dispplay_books(self, book):
        for book in self.books:
            print book

    def search_by_title(self, title: str):
        matching_books = []
        for book in self.books:
            if book.title == title:
            matching_books.append(book)
        return matching_books


