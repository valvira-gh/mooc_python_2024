
# We should validate input values that user gives
# With 'try' and 'exception' blocks we can validate the input,
# so that it's between 0 - 150 but also correct value. 

# try:
#     age = int(input("Enter your age: "))
# # In case of ValueError, the program executes 'except' block
# except ValueError:
#     age = -1

# if age >= 0 and age <= 150:
#     print("This is a fine age.")
# else:
#     print("This is not a valid age.")

#######################

# This program continues to ask the correct input value, even if there is a value error
def read_integer():
    while True:
        try:
            input_str = input("Please type in an integer: ")
            return int(input_str)
        except ValueError:
            print("This input is invalid")

number = read_integer()
print("Thank you!")
print(number, "to the power of three is", number**3)
