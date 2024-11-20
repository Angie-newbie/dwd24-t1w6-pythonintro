# print(2 + 3)

# # The below line prints Hello 
# print("Hello")

# print("Bye") #This line print Bye

# Data Types

# Numbers
# int
# 500
print(type(5))

# float
# 2.5
# 3.14159
print(type(3.14159))

# complex numbers
# 2 + 3j
print(type(2 + 3j))

#Number Operation
print(2 - 3)
print(5 * 2)
print(10 / 5) # / is Float Division
print(10 // 5) #// is integer division
print(10 // 3.5) # when have float, will stay float
print(5 % 2) #Modulo


# String
# "Hello World!"
# 'Hello World!' (But this will need '\' when print('it's monday'))
print("Hello World!")
print('it\'s monday')
print(type('hello'))

# Concatenation
print("Hello " + "World!")

# String methods
print("Hello".upper())
print("Hello world".lower())
print("Hello World".replace("World", "There"))

# Boolan
print(type(True))

# Falsy Values
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('ya'))
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))

# Comparison Operators
print(2 < 3)
print(2 > 3)
print(5 <= 5)
print(5 == 5)

# Logical Operators
# and, or, not
print(True and False)
print(True or False)
print(5 > 3 and 2 < 5)

# Variables
num1 = 5
num2 = 3
print(num1 + num2)
print (num1)
print (num2)
num2 = 11
print(num1 + num2)

# string interpolation
name = "Angie"
print("My name is " + name + " ya")
# f-string
print(f"My name is {name} and....")
