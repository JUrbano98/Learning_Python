'''
Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the output shall be
 "6 3 5 7", with a space separating the digits.
 '''


def invert_number(num):
    str_num = str(num)
    cont = 0
    while cont < len(str_num):
        print(str_num[-1-cont], end=" ")
        cont += 1


invert_number(2945)  # Expected "5 4 9 2"
