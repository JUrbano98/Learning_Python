'''
A palindrome number is a number that remains the same when its digits are
reversed. In simpler terms, it reads the same forwards and backward.
For example 121, 5005.

Write a code to check if given number is palindrome.
'''


def is_palindrome(num):
    original = num
    reversed = 0
    while num > 0:
        reversed = reversed*10 + num % 10
        num //= 10
    return print(original == reversed)


is_palindrome(123454321)  # Expected True
is_palindrome(5345893)  # Expected False
