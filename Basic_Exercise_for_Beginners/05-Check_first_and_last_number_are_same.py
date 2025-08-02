'''
Write a code to return True if the list’s first and last numbers are the same.
If the numbers are different, return False.
'''


def same_first_last(list_of_numbers):
    return (list_of_numbers[0] == list_of_numbers[-1])


print(same_first_last([10, 20, 30, 40, 10]))  # Expected True
print(same_first_last([75, 65, 35, 75, 30]))  # Expected False
