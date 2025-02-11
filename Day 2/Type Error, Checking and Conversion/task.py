# len(12345) - type error .... len() cannot accept integer value
len("12345")

# get the data type -- type checking
print(type("hello"))
print(type(123))
print(type(123.456))
print(type(True))

# change the data type -- type conversion
print(int("123")+ int("456"))
# int("abc") -- value error

# print("Number of letters in your name: " + len(input("Enter your name")))  -- fix the error in this line

print(type("Number of letters in your name: "))
name = input("Enter your name")
name_length = len(name)
print(type(name_length))

print("Number of letters in your name: " + str(len(input("Enter your name"))))
