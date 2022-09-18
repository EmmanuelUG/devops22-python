# ### `Exercise 1` even or odd

# Write a program that fulfills the specification:

# 1. Ask the user for a integer
# num = int(input("write a number:"))

# 2. If the integer is even, print even
# if (num % 2) == 0:
#     print("The number is even")
    
# # 3. If the integer is odd, print odd
# else:
#     print("odd")
# # ### `Exercise 2` VIP

# # Write a program that fulfills the specification:

# # 1. Ask the user for a name
# name = input("What is your name?:")
# print("Hello " + name)
# # 2. Create a tuple with at least five names
# names_tuple = ("Frank", "Emmanuel","Mani","Harry")
# # 3. If the user input is in the tuple, print the text "Welcome {name} your are on the list".
# if name in names_tuple:
#    print("Welcome " + name + " your are on the list")
# # Example 2
#    print(f"Welcome {name}  your are on the list")
# # print(f'"Welcome"{name}')
# # 4. If the user input is not in the tuple, print "Sorry, you are not on the list".
# else:
#    print("Welcome " + name + " your are not on the list")

# ### `Exercise 3` Repeat word

# Write a program that fulfills the specification:

# 1. Ask the user for a word
# from re import X


# word = input("Write a word:")


# # 2. Print the word x times, where x = len(word). i.e if the word is `hello` the program writes:
# # print(len(word))

# for _ in range(len(word)):
#     print(word)
    

#     ```text
#     hello
#     hello
#     hello
#     hello
#     hello
#     ```

# <div class="page"/>

# ### `Exercise 4` Sum

# Write a program that fulfills the specification:

# 1. Ask the user for a start and stop integer
# start_num = int(input("write a start and number:"))
# stop_num = int(input("write a stop number:"))

# # 2. Print every integer between start and stop. i.e. start = 1, stop = 5 would print:
# x = range(start_num, stop_num)
# for n in x:
#     print(n)

# #     ```text
# #     1
# #     2
# #     3
# #     4  
# #     ```

# # 3. Print the sum of all integers i.e
# total = sum(x)
# print(total)



#     ```text
#     Sum: 10
#     ```

# ### `Exercise 5` Until stop

# Write a program that fulfills the specification:

# 1. Create a while loop that runs forever
# x = 0
# while x < 0:
#     print(x)
#     x+=1
    


# x = 0
# while True:
#     print(x)
#     

# x = 0
# while True:
#      print(x)
#      x += 1
# 2. In each iteration, input a text
# x = "Emmanuel"
# while True:
#      print(x)
    
# 3. In each iteration, print a text "Enter `stop` to quit: "
# x = "Enter 'stop' to quit"
# while True:
#     print(x)
# 4. If the text equals stop, break the while loop
# from multiprocessing.resource_sharer import stop
# 5. If the text don't equals stop, print the text and the length of the text

from cgitb import text

while True:
    text =input("Enter'stop' to quit:")
    if text=="stop":
        break
    else:
        print(f'{text} {(len(text))}')
    

# ### `Extra exercise`

# See studentportalen `Extra_övningar_4.pdf`
