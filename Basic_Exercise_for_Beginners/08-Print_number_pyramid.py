'''
Print the following pattern:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''


def print_pyramid(n):
    for num in range(n):
        for i in range(num):
            print(num, end=" ")  # end=" " because usual end of a print is \n"
        print("\n")


print_pyramid(5)
