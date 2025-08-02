"""
Given two integer numbers, write a Python program to return their product
only if the product is equal to or lower than 1000.
Otherwise, return their sum.
"""


def mult_or_sum(num1: int, num2: int) -> int:
    result = num1*num2
    if result <= 1000:
        return result
    else:
        return num1 + num2


print("the result with 20 & 30 is -->", mult_or_sum(20, 30))
print("the result with 30 & 40 is -->", mult_or_sum(40, 30))
