#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter
# a 'quit' value . As they enter each topping, print a message saying you will add that topping to their pizza .


pizza_topping="\nEnter a Series of Pizza Topping"
pizza_topping +=" And Enter Quit When You are Finished"
while True:
    topping=raw_input(pizza_topping)
    if topping=='quit':
        break
    else:
        print("\n\nYou Add " + topping + ' Topping in Your Pizza')


#7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person age .
# If a person is under the age of 3, the ticket is free;
#if they are between 3 and 12, the ticket is $10; and
# if they are over age 12, the ticket is $15 .
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .

prompt="\nEnter Age To See the ticket Prices And Enter quit To Exit"
while True:
    age=raw_input(prompt)
    if age =='quit':
        break
    else:
        age=int(age)
        if age <=3:
            print("\nThe Ticket Is Free!!!")
        elif age >3 and age<=12:
            print("\nThe Ticket is $10 !!!")
        else:
            print("\nThe Ticket is $15 !!!")
