'''
Check if a user-entered string contains any digits using a for loop
'''


# Check if the string contains a digit
def digits_checker(str):
    for i in str:
        if '0' <= i <= '9':
            return False
    return True


# Function with input for the user
def string_checker():
    text = input("Enter a string: ")
    if digits_checker(text) is False:
        return print("The string has at least one number.")
    return print("The string doesn't have any number.")


string_checker()
