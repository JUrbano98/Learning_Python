'''
Write a Python code to display numbers from a list divisible by 5
'''


def divisibles_by_5(num_list):
    for i in num_list:
        if i % 5 == 0:
            print(i)


divisibles_by_5([10, 20, 33, 46, 55])  # Expected: 10, 20, 55
