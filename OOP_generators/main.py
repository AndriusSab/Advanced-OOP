# # Create a generator function that takes a positive integer n as input and generates all the even numbers up to and including n.


# def even_positive_integer_generator(n:int) -> int:
#      n = 0
#      while n
#                   yield n


# for n in positive_integer_generator(502):
#       print(n)


# even = []
# even_number = [even for x in range(15) if x % 2 == 0]

# from collections.abc import Iterator


# def even_number_generator(n: int) -> Iterator[int]:
#     while n >= 0:
#         even_numbers = [x for x in range(n + 1) if x % 2 == 0]
#         yield even_numbers
#         break
#     else:
#         print("number must be positive")


# for even_numbers in even_number_generator(15):
#     print(even_numbers)


# Create a generator function that would pick word from a generator and/list of generated random words (should be > 10000)
# and would stop itterating until the word longer than 7 lettters is found. Compare sizes of list and generator.
# Calculate performance per both executions (time to complete in ms)

from py_random_words import RandomWords
import sys


random_words = RandomWords()


word_generator_ls = [
    random_words.get_word() for word in range(1000) if len(random_words.get_word()) <= 7
]
word_generator_gc = (
    random_words.get_word() for word in range(1000) if len(random_words.get_word()) <= 7
)


print(f"List mem size is: {sys.getsizeof(word_generator_ls)})")
print(f"List mem size is: {sys.getsizeof(word_generator_gc)})")

print(word_generator_ls)
print(word_generator_gc)
