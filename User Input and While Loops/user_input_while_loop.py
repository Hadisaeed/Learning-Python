'''Most programs are written to solve an end users problem. To do so, you usually need to get some information
from the user. '''

#how the input() function works

#The input() function pauses your program and waits for the user to enter some text. Once Python receives the users
# input, it stores it in a variable to make it convenient for you to work with.The input() function takes one argument
# the prompt, or instructions, that we want to display to the user so they know what to do.

#message=raw_input("Tell Something, and I Will repeat it back to you: ")
#print(message)

#writing Clear Prompts

#Each time you use the input() function, you should include a clear, easy-tofollow prompt that tells the user exactly
# what kind of information you are looking for.

# name=raw_input("Please Enter Your Name: ")
# print("Hi, " + name + ' !')

#You can store your prompt in a variable and pass that variable to the input() function.

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = raw_input(prompt)
# print("\nHello, " + name + "!")

#Using int() to Accept Numerical Input

#When you use the input() function, Python interprets everything the user enters as a string.

# age=input(" How Old You Are? ")
# age=int(age)
# if (age >= 18):
#     print("True")
# else:
#     print("Flase")

#While Loop

#The for loop takes a collection of items and executes a block of code once for each item in the collection.
# In contrast, the while loop runs as long as, or while, a certain condition is true.

current_number=1
while current_number <= 5:
    print(current_number)
    current_number +=1

#letting the user choose When to quit

# prompt_1="Tell me somthing and i will repeat it back to you: "
# prompt_1 +="\nEnter 'Quit' to end the Program."
# user_message=''
# while user_message !='quit':
#     user_message=raw_input(prompt_1)
#     print(user_message)

#
# active=True
# while active:
#     user_message=raw_input(prompt_1)
#     if user_message=='quit':
#         active=False
#     else:
#         print(user_message)

# Using Break to Exit

#The break statement directs the flow of your program; you can use it to control which lines of code are executed and
# which are not, so the program only executes code that you want it to, when you want it to.

prompt="Please Enter The Name Of City You Have Visited: "
prompt +="\n(Enter Quit When You Are Finished.)"
while True:
    city=raw_input(prompt)
    if city=='quit':
        break
    else:
        print("I'd Love to go to " + city.title() + " !")

#Using continue in a Loop

#you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.

current_number1=0
while current_number1<10:
    current_number1 +=1
    if current_number1 % 2==0:
        continue                        # the continue statement tells Python to ignore the rest of the loop and return to the beginning.
    print(current_number1)

#using a while loop with lists and dictionaries

#Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and
# report on later.


unconfirmed_users=['hadi','pk','zain']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying User: " + current_user.title())
    confirmed_users.append(current_user)
print("'\n The Following Users have been Confirmed :")
for confirmed_user in confirmed_users:
    confirmed_user=confirmed_user.title()
    print(confirmed_user)

#Removing  Instances of Specific Values from a List

pets=['dog','cat','goldfish','rabbit']
print(pets)
while 'goldfish' in pets:
    pets.remove('goldfish')
print(pets)

#Filling a Dictionary with User input

responses={}
polling_active=True
while polling_active:
    name=raw_input("\nWhat is Your Name?")
    response=raw_input("\nWhich Mountian Would You Like To Climb Someday?")
    responses[name]=response
    repeat=raw_input("\nWould You Like to let another person respond? (Yes/no)")
    if repeat=='no':
        polling_active=False
print("\n ====== Polling Results ======")
for name,response in responses.items():
    print(name + " Would Like to Climb " + response + " .")