import random
# List containing numbers 1-50
numbers_list = list(range(1, 51))

# Random sentence
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and easy-to-learn programming language.",
    "Life is what happens when you're busy making other plans.",
    "Coding is like solving a puzzle with infinite possibilities.",
    "She sells seashells by the seashore."
]

random_sentence = random.choice(sentences)
# print("Numbers List:", numbers_list)
# print("Random Sentence:", random_sentence)

# Task: List Comprehension Practice
# You are given a list of numbers. Your goal is to complete the following tasks using list comprehensions:

# Create a new list containing only the even numbers from the original list.
odd_list = [x for x in numbers_list if x % 2 != 0]
print(odd_list)

# Create a new list containing the squares of the even numbers from the original list.
even_squares = [x ** 2 for x in numbers_list if x % 2 == 0]
print(even_squares)

# Create a new list containing only the numbers that are divisible by 3 but not by 5 from the original list.
divisable_by_three = [x for x in numbers_list if (x % 3 == 0 and x % 5 != 0)]
print(divisable_by_three)

# Create a new list containing the words in a sentence that are longer than 4 characters (ignoring case).
four_or_more = [str for str in random_sentence.split(" ") if len(str)> 4]
print(four_or_more)

# Create a new list containing the first letter of each word in a sentence (ignore punctuation).
first_letters = [str[0] for str in random_sentence.split(" ")]
print(first_letters)




#  Retain order and remove duplication
# old_list = ["A", "A", "B", "C", "B", "A", "C"]
# new_list = list(dict.fromkeys(old_list))
# print(new_list)

# my_new_list = [x for x in range(1,6)]
# print(my_new_list)

# standard_dict = {x: [x for x in range(1,6)] for x in range(1,6)}
# print(standard_dict)

# squared_list = [x ** 2 for x in range(1,6)]
# print(squared_list)

# filtered_list = [x ** 2 for x in range(1,6) if x % 2 == 0]
# print(filtered_list)