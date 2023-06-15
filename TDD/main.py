# TDD: Fizz buzz is a group word game for children to teach them about division.
# Players take turns to count incrementally,
# replacing any number divisible by three with the word "fizz", 
# and any number divisible by five with the word "buzz", 
# and any number divisible by both 3 and 5 with the word "fizzbuzz".

import random

class FizzBuzz:
    
    def __init__(self, number: int):
        self.number = number
    
    def division_by_three(self):
        if self.number % 3 == 0:
            return "fizz"
        
    
    def division_by_five(self):
        if self.number % 5 == 0:
            return "buzz"
        
    
    def division_by_three_and_five(self):
        if self.number % 3 == 0 and self.number % 5 == 0:
            return "fizzbuzz"
        
    
    def check_answer(self, answer):
        fizz = self.division_by_three()
        buzz = self.division_by_five()
        fizzbuzz = self.division_by_three_and_five()
        
        if (fizz and answer == "fizz") or (buzz and answer == "buzz") or (fizzbuzz and answer == "fizzbuzz"):
            return True
        else:   
            return False

    

if __name__ == "__main__":
    number = random.randint(1, 100)
    fizz_buzz = FizzBuzz(number=number)
    
    print(number)
    while True:
        user_answer = input("Please choose the correct answer: fizz, buzz, or fizzbuzz: ")
        if user_answer not in ["fizz", "buzz", "fizzbuzz"]:
            print (ValueError, "choose answer from fizz, buzz  and fizzbuz")
        else:
            break
            
        
    is_correct = fizz_buzz.check_answer(user_answer)
    
    if is_correct:
        print("Your answer is correct!")
    else:
         print("Your answer is incorrect.")
    
    # fizz = fizz_buzz.division_by_three()
    # buzz = fizz_buzz.division_by_five()
    # fizzbuzz = fizz_buzz.division_by_three_and_five()
    
    # print(fizz)
    # print(buzz)
    # print(fizzbuzz)