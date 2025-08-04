'''
Print Alternate Prime Numbers till 20
A Prime Number is a number that can only be divided
by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
'''

import math


# Firstly a method to check if a number is prime or not
def is_prime(num):
    if num <= 1:
        prime = False
    else:
        prime = all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
    return (prime)


# Secondly the printer method for the first n numbers (only even primes)
def primes_printer(nums):
    result = []
    for i in range(nums):
        if is_prime(i):
            result.append(i)
    return result[::2]


print(primes_printer(20))
