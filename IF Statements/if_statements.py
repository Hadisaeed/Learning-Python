# if statement allows you to examine the current state of a program and respond appropriately to that state.
cars=['bmw','audi','toyota']
for car in cars:
    if car=='audi':
        print(car.upper())
    else:
        print(car.title())
# if statement is an expression that can be evaluated as True or False and is called a conditional test.


# users=["Pk","hadi","Ramsha"]
# name=raw_input("Enter User Name ...")
# name=name.lower()
# print name
# for user in users:
#     if name==user:
#         print("User is Exit !!! ")
#     else:
#         print("User is not Exit !!!")
#Checking for Inequality

requested_topping='mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

answer=20
if answer!=42:
    print("That's not a Correct Answer.Please try Again!!")

#Checking Whether a Value Is in a List

# name=['Pk','Hadi','Ali']
# u_name=raw_input("\nEnter the You Want To Check In the List... ")
# u_name=u_name.title()
# if u_name in name:
#     print("Record is Found !!!")
# else:
#     print("Record is Not Found!!!")

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#if-else Statements

age=17
if age>=18:
    print("\nYou are Old Enough to Vote !!! ")
    print("\nHave you Rgistered to Vote Yet???")
else:
    print("\nYour are too young to Vote.")
    print("\nPlease register to vote as soon as you turn 18!")

#The if-elif-else Chain

age=19
if age<4:
    print("\nYour Admission Cost is 0$. ")
elif age<18:
    print("\nYour Admission Cost is 5$. ")
else:
    print("\nYour Admission Cost is 10$. ")

age_1=12

if age_1<4:
    price=5
elif age_1<18:
    price=15
elif age_1<65:
    price=20
else:
    price=5
print("Your Admission Cost is $:" +str(price) +".")
