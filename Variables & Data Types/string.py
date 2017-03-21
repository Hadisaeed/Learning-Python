"""A string is simply a series of characters. Anything inside quotes is considered a string in Python,
and you can use single or double quotes around your strings"""
string_one='This is String !!!'
string_two="This is also an String !!!"
print string_one
print string_two


#String Methods
# A method is an action that Python can perform on a piece of data.

name="muhammad hadi saeed"
print(name)

#title() displays each word in titlecase, where each word begins with a capital letter.
print(name.title())

#upper() display each letter in capital case.

print(name.upper())

#lower() display each letter in lower Case.

case="TEST"
print(case.lower())

#Concatenation Of Strings
#The Method of combining strings is called Concatenation.Python uses the plus symbol (+) to combine strings.

first_name="hadi"
last_name=" saeed"
full_name=first_name + last_name
print("Full Name is :",full_name.title())


#Python can look for extra whitespace on the right and left sides of a string.
#To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
lang=" Python "
print("Language:", lang)
lang=lang.rstrip()
print("Language",lang)
#To ensure that no whitespace exists at the left end of a string, use the lstrip() method.
lang_1=" Python 2 "
print("Language 1:", lang_1)
lang_1=lang_1.lstrip()
#To ensure that no whitespace exists at the right & Leftend of a string, use the strip() method.
print("Language",lang_1)
print ("Language:", lang.strip())

