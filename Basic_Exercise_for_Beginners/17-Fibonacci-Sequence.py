'''
Fibonacci Sequence is a series of numbers in which the next number is found
by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series
is 13 + 21 = 34.
'''


def fibonacci(n):
    num1, num2 = 0, 1
    for i in range(n):
        print(num1, end=" ")
        res = num1 + num2

        num1 = num2  # Recursive idea
        num2 = res


fibonacci(15)
