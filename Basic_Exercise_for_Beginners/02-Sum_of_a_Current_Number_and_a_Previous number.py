'''
Write Python code to iterate through the first 10 numbers and, in each
iteration, print the sum of the current and previous number.
'''


def sum_of_curr_and_actual_number():
    prev = 0
    for i in range(1, 10):
        sums = prev + i
        print("Current number: ", i, ", previous: ", prev,
              "Sum of both: ", sums, ".")
        prev += 1


sum_of_curr_and_actual_number()
