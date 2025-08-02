'''
Write a Python code to check if the given number is a palindrome. A palindrome
number reads the same forwards and backward. For example, 545 is
a palindrome number.
'''


def is_palindrome(num):
    string_num = str(num)
    return string_num == string_num[::-1]


print(is_palindrome(123676321))  # Expected True
print(is_palindrome(1200321))  # Expected False
