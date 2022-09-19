# # Exercise Lesson 7

# ## Instructions

# Todays exercises goal is to learn about basic functions.

# ### `Exercise 1` Functions

# 1. Create a function with name `do_nothing`
#    1. The function should have a `pass`
#    2. Call the function from your code
# 2. Functions getting started:
#    1. Create a function that prints `hello world`
#    2. Create a function that prints the result from `1 == 1.0`
#    3. Create a function that prints the alphabet in reverse order



from audioop import reverse
from ctypes.wintypes import WORD
import string



def do_nothing():
    pass
do_nothing()

# def say_hello():
#     print("hello world")
# say_hello()

# def one_one():
#     print("1 == 1.0")

# one_one()


import string
# def rev_Alpha():
#     print(string.ascii_lowercase[::-1])


# rev_Alpha("word")





# 3. Functions with arguments
#    1. Create a function that prints `hello name` with name as a parameter
#    2. Create a function that prints a string in capital letters, with `word` as a parameter
#    3. Create a function that prints numbers between 1 and `stop`, where stop is a parameter


# example for testing return
# def my_name():
#     return "Hello name"  
# print(my_name()) 

# def name(name):
#     print(f'hello {name}')
    
# name("Frank")

# example import from W3school
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# example for testing return with uppercase
# def capital_letter():
#     return "Word"

# print(capital_letter().upper())


# def cap(word):
#     print(word.upper())
      
# cap("word")
    
 
# def num_prints(stop):
#     print(list(range(1, stop))) 
    
# num_prints()

    
# ### `Exercise 2` Default Arguments

# 1. Create a function that prints 1 to 10 by default, i.e `start=1` `stop=11` and uses a range in the function block.
# 2. Create a function that by default prints a string, if `reverse=True` is used as argument the string is printed in reverse.
# 3. Call the same function with and without reverse

def default_one_to_ten(start=1, stop=11):
    print(list(range(start, stop)))

    
default_one_to_ten()

def rev_word(word, reverse=False):
    if reverse:
        word=word[::-1]
        
rev_word(hello word, reverse=True)
    
# ### `Exercise 3` Return

# 1. Create a function that returns a integer
# 2. Create a function that returns a tuple with (x, y) value
# 3. Create a function that returns a boolean value
# 4. Create a function that returns a float
# 5. Create a function that has `firstname` and `lastname` as parameters and returns fullname.
# 6. Create a function that calculates the area of a rectangle and returns the result
# 7. Create a function that expects a list as argument, the list should contain integers and the function should return the sum of all elements in the list.
# 8. Create a function that repeats a word multiple time, `word` and `repeat` is used as parameters. If the word is hello and repeat is 3, it will print hello three times.



