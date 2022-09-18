# 1. Generate a list containing the numbers 1, 2, 3 to 100.   
# 2. Generate a list of all even numbers from 2 to 60
# 3. Generate a list of all odd numbers from 1 to 77
# 4. Generate a list of 100 numbers between 1 - 300
#     1. The numbers must be unique
#     2. The numbers are selected randomly (not unique)
# 5. create a list containing five colors (not containing red)
#    1. Create a new list containing "red" and also add two colors by random with `choice`, `choices` or `sample` from the list.
#    2. Generate a list of random colors from the list of 3, the list should be of length 50.
#    3. Print the length of all three lists and the unique colors in each list

# one_to_hundred = [x for x in range(2,101)]
# print(one_to_hundred)
# test for even numbers in included in exercises
# for num in one_to_hundred:
#    if num % 2==0:
#     print(num, end=" ")
# list_of_even = [num for num in range(2,61,2)]
# print(list_of_even)
# list_of_odd = [num for num in range(1,79,2)]
# print(list_of_odd)
# one_to_tre_hundred = [x for x in range(1,301)]
# print(one_to_tre_hundred)

    # for x in one_to_tre_hundred:
        # if x not in unique_one_to_tre_hundred:
            
        

  
# Function to get unique values
  
  
# def unique(one_to_tre_hundred):
  
#     # Print directly by using * symbol
#     print(*Counter(one_to_tre_hundred))
  
  
# driver code
# one_to_tre_hundred = [x for x in range(1,301)]
# print("the unique values from 1st list is")
# unique(one_to_tre_hundred)
 
# list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
# print("\nthe unique values from 2nd list is")
# unique(list2)
# list1 = list(range(1,101))
# list_of_even = list(range(2,61,2))
# list_of_odd = list(range(1,78,2))
# print(list_of_odd)
# list_of_hundred =list(range(1,300))
# print(list_of_hundred(random.random))


# import random
 
# random.seed(300)
# print(random.random())

# from random import sample

#     population = list(range(1, 301))
#     hundred_numbers = sample(population, k=100)
#     print(hundred_numbers)

# from unittest import result

# import random
import string
from operator import mul
from random import random, shuffle, choices, sample
from typing import Counter

colors1 = ['Green', 'Black', 'Yellow', 'Orange', 'Pink']
colors2=choicescolors1['Red'],k=2)
print(colors2)
# result = random.choices(colors1, k=10)
# print(result)