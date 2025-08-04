'''
Print the following pattern:

1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''


# This exercise is similar to 08-Print_number_pyramid
def print_pyramid_inverse(n):
    for num in range(1, n + 1):
        for i in range(n - num + 1):
            print(num, end=" ")  # end=" " because usual end of a print is \n"
        print("\n")


print_pyramid_inverse(5)
