#write a program that whict takes a number input through user and tell him the number is even or odd?

# number=raw_input("Enter a Number, I'll Tell You the Number is Even OR Odd: ")
# number=int(number)
# if number%2==0:
#     print("\n The Number " + str(number) + " is Even.")
# else:
#     print("\n The Number " + str(number) + " is Odd.")

#7-1. Rental Car: Write a program that asks the user what kind of rental car they would like . Print a message about
# that car, such as Let me see if I can find you a Subar.

# rental_car=raw_input("What Kind of Rental Car You Would Like? ")
# print("Let me See If I Can Find You a " + str(rental_car))

#7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group .
# If the answer is more than eight, print a message saying they will have to wait for a table . Otherwise,
# report that their table is ready .

# numbers_of_people=raw_input("How Many People are in Dinner Group? ")
# numbers_of_people=int(numbers_of_people)
# if numbers_of_people >=8:
#     print("You have to wait for a table.")
# else:
#     print("Your Table is Ready!!!")

#7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .

input_number=raw_input("Enter a Number!!! ")
input_number=int(input_number)
if input_number%10==0:
    print("The " + str(input_number)+ " is Multiple of 10 ")
else:
    print("The " + str(input_number)+ " is Not Multiple of 10 ")