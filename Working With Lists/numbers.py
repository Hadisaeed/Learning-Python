#Printing numbers from 1 to 10
print("Printing Numbers From 1 to 10\n")
for numbers in range(1,11):
    print(numbers)
#Printing numbers in reverse Order
print("Printing Numbers From 20 to 1\n")
for numbers in range(20,0,-1):
    print(numbers)
#printing String  10 times
name="Muhammad Hadi Saeed"
for nam in range(1,11):
    print(name)
#Using range() to Make a List of Numbers
print("\nMake A List Of Numbers")
num=list(range(1,6))
print(num)

#generating Even Numbers From 0 to 20
print("\nGenerating Even Numbers From 0 to 20:\n")
even_num=range(0,21,2)
print(even_num)

#generating odd Numbers From 1 to 20
print("\nGenerating odd Numbers From 0 to 20:\n")
od_num=range(1,21,2)
print(od_num)

#Printing squares of numbers from 1 to 10
print("\nPrinting squares of numbers from 1 to 10")
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)

#Printing cubes of numbers from 1 to 10
print("\nPrinting Cubes of numbers from 1 to 10")
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
    print(cubes)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("The Digits Are:\n" ,digits)
print("The Minimum value is: ",min(digits))
print("The Maximum value is: ",max(digits))
print("The Sum Of Numbers is: ",sum(digits))

#List Comprehension Important
squares = [value**2 for value in range(1,11)]
print(squares)

#4-7
cubes = [value**3 for value in range(1,11)]
print(cubes)

#slicing a List

friends=['Zobia','Hadi','Faizan','Pk','Nisha']
print(friends[0:3])
print(friends[2])
print(friends[3:])
for frnd in friends[0:2]:
    print(frnd.title())


friends=['Zobia','Hadi','Faizan','Pk','Nisha']
print(friends[0:3])
print(friends[1:4])
print(friends[-3:])
#Tuples
print("Working With Tuples")
dimensions=(200,300,500)
print(dimensions[1])
print(dimensions[2])

print("The Oriinal dimensions:")
for dimension in dimensions:
    print(dimension)
print("Modified dimension:\n")
dimensions=(450,.800,100)
for dim in dimensions:
    print(dim)






