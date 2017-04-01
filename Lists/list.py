#creating a list

bicycle=['trel','cannondale','redline','specialized']
print(bicycle)

#Accessing Elements in a List
# Lists are ordered collections, so you can access any element in a list by telling Python
# the position, or index, of the item

print(bicycle[0])
print(bicycle[3])
print(bicycle[2])
#print 2 element of list in title case.

print(bicycle[2].title())

print(bicycle[-1])
print(bicycle[-4])
print(bicycle[-2])

# Store the names of a few of your friends in a list called names . Print each persons name by accessing each element
# in the list, one at a time .

friends=['Zain','PK','Hadi','Jamal']
print("Friend 1 :", friends[1])
print("Friend 2 :", friends[0])
print("Friend 3 :", friends[3])
print("Friend 4 :", friends[2])

#Start with the friends list but instead of just printing each persons name, print a message to them .
#  The text of each message should be the same, but each message should be personalized with the persons name .

print("Hi, " + friends[1] + " Would You Like To Learn Some Python ? ")
print("Hi, " + friends[3] + " Would You Like To Learn Some Python ? ")
print("Hi, " + friends[2] + " Would You Like To Learn Some Python ? ")
print("Hi, " + friends[0] + " Would You Like To Learn Some Python ? ")


#Changing, Adding and Removing Elements

#Modifying elements in a list

motorcycles=['ducati','yamaha','Suzuki']
print(motorcycles)
motorcycles[0]='honda'
print(motorcycles)

#The append() method adds element to the end of the list without affecting any of the other elements in the list

motorcycles.append('ducati')
print(motorcycles)

#You can add a new element at any position in your list by using the insert()method.

motorcycles.insert(2,'BMW')
print(motorcycles)

#Removing element From List

#Removing an Item Using del Statement

del motorcycles[4]
print(motorcycles)

#Removing an Item using Pop Method

#The pop() method removes the last item in a list, but it lets you work with that item after removing it.
# The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack.

motors=['Suzuki', 'Toyota' ,'Yamaha']
print("Motors :" ,motors)
poped_motors=motors.pop()
print("Poped Motor: ",poped_motors)
print("Motors",motors)
last_own=motors.pop()
print("The last Motor I Own Was a " + last_own.title()+ ".")
print("Motors",motors)
first_own=motors.pop()
print("The First Motor I own Was a " + first_own.title() + ".")
print("Motors",motors)

#reassigning Motors

motors=['BMW', 'Tesla','Honda']
print("Motors After Reassigning:",motors)

#poping items from Any Position in a list

fav_motor=motors.pop(1)
print("My Favourite Motor is ",fav_motor)
print("Motors:",motors)
motors.append('Toyota')
print("Motors:",motors)

#Removing an Item by Value
motors.remove('BMW')
print("Motors:",motors)



#Sorting a list Permanently with the Sort() Method

cars=['BMW','Audi','Toyota','subaru']
print("Cars Before Sort Method: ",cars)
cars.sort()
print("Cars after Sort Method: ",cars)

numbers=[5,1,10,2,4,7,3,8,9,6]
print("Numbers Before Sort:",numbers)
numbers.sort()
print("Numbers After Sort:",numbers)
print(numbers)
#You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
numbers.sort(reverse=True)
print("Number Sorted in Reverse Order: ",numbers)

#Sorting a List Temporarily with sorted() function

n_cars=['BMW','Audi','Toyota','subaru']
print("Here is the Original List: ")
print(n_cars)
print("\nHere is the Sorted List: ")
print(sorted(n_cars))
print("\nHere is the Original List again: ")
print(n_cars)

#Printing a List in Reverse Order

print("Original Order Of List:")
print(n_cars)
n_cars.reverse()
print("Reverse Order of List:")
print(n_cars)

#finding the length of List
print(len(n_cars))