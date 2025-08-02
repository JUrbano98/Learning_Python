'''
Print a downward half-pyramid pattern of stars:

* * * * *
* * * *
* * *
* *
*
'''


def down_pyramid(n):
    cont = n
    while cont > 0:
        for i in range(cont):
            print("*", end=" ")  # end=" " 'cause usual end of a print is \n"
        print("\n")
        cont -= 1


down_pyramid(5)
