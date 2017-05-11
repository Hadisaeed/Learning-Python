#7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches . Loop through the list of sandwich orders and
# print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches .
# After all the sandwiches have been made, print a message listing each sandwich that was made .

# sandwitch_order=['club','chicken','vegitable','tuna']
# finished_sandwitces=[]
# for sandwitch in sandwitch_order:
#     print("I made your " + sandwitch.title() +" Sandwitch")
#     finished_sandwitces.append(sandwitch)
# print("\n********** MADE SANDWITCHES **********")
# for made_sandwitch in finished_sandwitces:
#     made_sandwitch=made_sandwitch.title()
#     print(made_sandwitch)


# 7-8 and My Own version

# made_sandwitches=[]
# order=True
# while order:
#     sandwitch_order=raw_input("Enter Your Sandwitch Order")
#     print("I Made Your " + sandwitch_order +" Sandwitch")
#     made_sandwitches.append(sandwitch_order)
#     repeat=raw_input("More Sandwitch Order? (Yes/No)")
#     if repeat =='no':
#         order=False
# print("\n ---------- Your Ordered Sandwitches are: ----------")
# for order_sandwitches in made_sandwitches:
#     order_sandwitches=order_sandwitches.title()
#     print(order_sandwitches)

#7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in
# the list at least three times .
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders .
# Make sure no pastrami sandwiches end up in finished_sandwiches .

print(" !!!! Deli has Run Out of Pastrami Sandwitch !!!!")
made_sandwitches=[]
order=True
while order:
    sandwitch_order=raw_input("Enter Your Sandwitch Order")
    print("I Made Your " + sandwitch_order +" Sandwitch")
    if sandwitch_order =='pastrami':
        print(" !!!! Sorry Pastrami Sandwitch Run Out !!!!")
    made_sandwitches.append(sandwitch_order)
    while 'pastrami' in made_sandwitches:
      made_sandwitches.remove('pastrami')
    repeat=raw_input("More Sandwitch Order? (Yes/No)")
    if repeat =='no':
        order=False
# while 'pastrami' in made_sandwitches:
#     made_sandwitches.remove('pastrami')
print("\n ---------- Your Ordered Sandwitches are: ----------")
for order_sandwitches in made_sandwitches:
    order_sandwitches=order_sandwitches.title()
    print(order_sandwitches)

#7-10. Dream Vacation: Write a program that polls users about their dream vacation .
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll .

vactions={}
flag=True
while flag:
    users=raw_input("\n\nEnter Your Name ")
    dream_vacation=raw_input(users + ", " + " If you could visit one Place in the world, Where would you go?")
    vactions[users]=dream_vacation
    next_user=raw_input("\nWould You like to poll another user? (yes/no)")
    if next_user == 'no':
        flag=False
print("\n---------- Polling Results ----------")
for user,dream_vacation in vactions.items():
    print("\n" + user.title() + " Dream Place in the World is " + dream_vacation.title())

