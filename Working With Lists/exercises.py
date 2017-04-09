#4-1. Pizzas: Think of at least three kinds of your favorite pizza . Store these pizza names in a list, and
# then use a for loop to print the name of each pizza .
# 1.Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza .
# For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza .
# 2.Add a line at the end of your program, outside the for loop, that states how much you like pizza .
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence,
# such as I really love pizza!

print("Example 4-1\n")
pizzas=['Beefy Sensation','Chicken Fajita','Veggie Lover']
print("Name of Pizzas:\n")
for names_of_pizza in pizzas:
    print(names_of_pizza + "\n")
for pizza in pizzas:
    print(pizza)
    print("I Like " + pizza + " So Much!!!\n")
print("I Really Like Pizza")
print(pizzas[1]+ " with extra Toppings is my Favourite Pizza")
print("I Really Love Pizza!")

#4-2. Animals: Think of at least three different animals that have a common characteristic .
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal .
# 1.Modify your program to print a statement about each animal, such as A dog would make a great pet.
# 2.Add a line at the end of your program stating what these animals have in common .
# You could print a sentence such as Any of these animals would make a great pet!print
print ("EXAMPLE 4-2")
animals=['Noplean','Snowball','Squealer']
for animal in animals:
    print(animal)
    print("A "+ animal + " would make a great pet")
print("\nAll these Animal one thing in Common:")
print("They all Are Good Pets!!")

#4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five simple foods, and store them in a tuple
#  1.Use a for loop to print each food the restaurant offers .
#  2.Try to modify one of the items, and make sure that Python rejects the change .
#  3.The restaurant changes its menu, replacing two of the items with different foods .
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu .

foods=("Soups ","Cheese","Pasta and Rice","Salad Dressings","Zinger")
print(foods)
print("Restaurant Offers Following foods:")
for food in foods:
    print(food)
#foods[0]="Cheese Burger"
#print(foods[0])
print("Restaurant Replace Two foods:")
foods=("Pizza","Cheese Burger","Pasta and Rice","Salad Dressings","Zinger")
for food in foods:
    print(food)
