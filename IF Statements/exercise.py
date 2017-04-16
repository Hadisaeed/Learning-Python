#practice Example
# print("Selection Criteria of Vollay ball Player")
# age=int(input("Enter Your Age ... "))
# height=int(input("Enter Your Height ..."))
# if(age >20) and (height >=6):
#     print("Congraulation You are Selected ")
# else:
#     print("Sorry, You are not Selected")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a persons stage of life .
# Set a value for the variable age, and then:
# If the person is less than 2 years old, print a message that the person is a baby .
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler .
# If the person is at least 4 years old but less than 13, print a message that the person is a kid .
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager .
# If the person is at least 20 years old but less than 65, print a message that the person is an adult .
# If the person is age 65 or older, print a message that the person is an elder .
#
# age=int(input("Enter Your Age ... "))
# if age<2:
#     print("The Person is a Baby. ")
# elif (age==2 or age<4):
#     print("The Person is a Toddler.")
# elif (age==4 or age<13):
#     print("The Person is a Kid.")
# elif (age==13 or age<20):
#     print("The Person is a Teenager.")
# elif (age==20 or age<65):
#     print("The Person is an Adult.")
# elif (age>=65):
#     print("The Person is an Elder.")
#
# #
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that
# check for certain fruits in your list .
# 1. Make a list of your three favorite fruits and call it favorite_fruits .
# 2. Write five if statements . Each should check whether a certain kind of fruit is in your list .
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!

# favorite_fruits=['mango','apple','banana']
# fruit=raw_input("Enter Fruit ... ")
# if fruit in favorite_fruits:
#     print("Your Fruit is in the List.")
# else:
#     print("Your Fruit is not in List. ")
# if fruit=='mango':
#     print("You Love Mangoes!!! ")
# if fruit=='apple':
#     print("You like Apple!")
# if fruit=='banana':
#     print("You really like Bananas!")

# 5-8 & 5-9. Hello Admin: Make a list of five or more usernames, including the name 'admin' .
# Imagine you are writing code that will print a greeting to each user after they log in to a website .
# Loop through the list, and print a greeting to each user:
# 1.If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# 2.Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

# username=['admin','hadi','pk','ali','zain']
# p_name=raw_input("Enter Your Name .. ")
# if not username:
#     print('We need to find some user')
# elif p_name in username and p_name=='admin':
#     print("Hello " + p_name + " Would you like to see a status report? ")
# else:
#     print("Hello " + p_name + " thank you for logging in Again.")

# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a
# unique username .
# 1.Make a list of five or more usernames called current_users .
# 2.Make another list of five usernames called new_users . Make sure one or two of the new usernames are also in the
# current_users list .
# 3.Loop through the new_users list to see if each new username has already been used . If it has, print a message that
# the person will need to enter a new username . If a username has not been used, print a message saying that
# the username is available .
# 4.Make sure your comparison is case insensitive . If 'John' has been used, 'JOHN' should not be accepted .

# current_users=['hadi','pk','ali','rehana','sadia']
# new_users=['alexa','hadi','pk','yasir','ayesha','ramsha']
# for new_user in new_users:
#     new_user.lower()
#     if new_user in current_users:
#         print(new_user + " You need to enter a new username")
#     else:
#         print(new_user + " The username is available")

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd .
# Most ordinal numbers end in th, except 1, 2, and 3 .
# 1.Store the numbers 1 through 9 in a list .
# 2.Loop through the list .
# 3.Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number .Your output should
# read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line .
ordinal_numbers=raw_input("Enter Ordinal Numbers from 1 to 9 in a Sequence with Comma separated : ")
list=ordinal_numbers.split(',')
print list
for n in list:
    if n=='1':
        print("1st")
    elif n == '2':
        print("2nd")
    elif n == '3':
        print("3rd")
    elif n == '4':
        print("4th")
    elif n == '5':
        print("5th")
    elif n == '6':
        print("6th")
    elif n == '7':
        print("7th")
    elif n == '8':
        print("8th")
    elif n == '9':
        print("9th")


