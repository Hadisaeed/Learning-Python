#3-4. If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least
# three people you had like to invite to dinner Then use your list to print a message to each person, inviting
#them to dinner
print("\nExample 3-4")
invitation_list=['Pk','ali','Ahmed']
print("Hi, " +invitation_list[0] +" Would you Like to Come home For dinner At 9PM ?" )
print("Hi, " +invitation_list[1] +" Would you Like to Come home For dinner At 9PM ?" )
print("Hi, " +invitation_list[2] +" Would you Like to Come home For dinner At 9PM ?" )

#3-5. Changing Guest List: You just heard that one of your guests cannot make the
#dinner, so you need to send out a new set of invitations You will have to think of someone else to invite
#Start with your program from Exercise 3-4 Add a print statement at the end of your program stating the name of the
# guest who cannot make it
#Modify your list, replacing the name of the guest who cannot make it with the name of the new person you are inviting
#Print a second set of invitation messages, one for each person who is still in your list
print("\nExample 3-5")
print(invitation_list[1], " Can not Make the Dinner ")
del invitation_list[1]
invitation_list.insert(1,'Hadi')
print("Hi, " +invitation_list[1] +" Would you Like to Come home For dinner At 9PM ?" )

#3-6. More Guests: You just found a bigger dinner table, so now more space is available Think of three more guests to
# invite to dinner
#Start with your program from Exercise 3-4 or Exercise 3-5 Add a print statement to the end of your program informing
# people that you found a bigger dinner table
#Use insert() to add one new guest to the beginning of your list
#Use insert() to add one new guest to the middle of your list
#Use append() to add one new guest to the end of your list
#Print a new set of invitation messages, one for each person in your list
print("\nExample 3-6")
print("I Found a Bigger Dinner Table")
invitation_list.insert(0,'Umair')
invitation_list.insert(3,'yasir')
invitation_list.append('Asim')
print("Hi, " +invitation_list[0] +" Would you Like to Come home For dinner At 9PM ?" )
print("Hi, " +invitation_list[1] +" Would you Like to Come home For dinner At 9PM ?" )
print("Hi, " +invitation_list[2] +" Would you Like to Come home For dinner At 9PM ?" )
print("Hi, " +invitation_list[3] +" Would you Like to Come home For dinner At 9PM ?" )
print("Hi, " +invitation_list[4] +" Would you Like to Come home For dinner At 9PM ?" )
print("Hi, " +invitation_list[5] +" Would you Like to Come home For dinner At 9PM ?" )

#3-7. Shrinking Guest List: You just found out that your new dinner table would not arrive in time for the dinner, and
# you have space for only two guests
# Start with your program from Exercise 3-6 .
# Add a new line that prints a message saying that you can invite only two people for dinner .
# Use pop() to remove guests from your list one at a time until only two names remain in your list .
# Each time you pop a name from your list, print a message to that person letting them know you are sorry you can not
# invite them to dinner .
# Print a message to each of the two people still on your list, letting them know they are still invited .
# Use del to remove the last two names from your list, so you have an empty list .
# Print your list to make sure you actually have an empty list at the end of your program .
print("\nExample 3-7")
print(invitation_list)
pop_invitation_list=invitation_list.pop()
print(pop_invitation_list + " Sorry Your not invited!")
pop_invitation_list=invitation_list.pop()
print(pop_invitation_list + " Sorry Your not invited!")
pop_invitation_list=invitation_list.pop()
print(pop_invitation_list + "Sorry Your not invited!")
pop_invitation_list=invitation_list.pop()
print(pop_invitation_list + " Sorry Your not invited!")
print("Hi ",invitation_list[0] + " You are Still Invited!!")
print("Hi ",invitation_list[1] + " You are Still Invited!!")
print(invitation_list)
del invitation_list[0]
print(invitation_list)
del invitation_list[0]
print(invitation_list)

#3-8. Seeing the World: Think of at least five places in the world you had like to visit .
# 1.Store the locations in a list . Make sure the list is not in alphabetical order .
# 2.Print your list in its original order . Don not worry about printing the list neatly, just print it as a raw Python list .
# 3.Use sorted() to print your list in alphabetical order without modifying the actual list .
# 4.Show that your list is still in its original order by printing it .
# 5.Use sorted() to print your list in reverse alphabetical order without changing the order of the original list .
# 6.Show that your list is still in its original order by printing it again .
# 7.Use reverse() to change the order of your list . Print the list to show that its order has changed .
# 8.Use reverse() to change the order of your list again . Print the list to show its back to its original order .
# 9.Use sort() to change your list so its stored in alphabetical order . Print the list to show that its order has been changed .
# 10.Use sort() to change your list so its stored in reverse alphabetical order . Print the list to show that its order has changed .
print("\nExample 3-8")
#1
world_places=['The Golden Gate Bridge','Eiffel Tower','Wall of China','Taj Mahal','Stonehenge']
#2
print("\nWorld Places List In Original Order:")
print(world_places)
#3
print("\nSorted World Places List In Original Order:")
print(sorted(world_places))
#4
print("\nWorld Places List In Original Order:")
print(world_places)
#5
print("\nWorld Places List in Reverse Order:")
print(sorted(world_places,reverse=True))
#6
print("\nWorld Places List In Original Order:")
print(world_places)
#7
world_places.reverse()
print("\nThe Original List is Now Modified:")
print(world_places)
#8
world_places.reverse()
print("\nThe Modified List is Now Back To Original Order:")
print(world_places)
#9
world_places.sort()
print("\nThe List Order Now Change:")
print(world_places)
#10
world_places.sort(reverse=True)
print("\nThe List is Now Reverse Order:")
print(world_places)