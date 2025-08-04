'''
Capitalize the first letter of each word in a string.
'''


def capitalizer(text):
    cont = 0
    result = ""
    while cont < len(text):
        if text[cont - 1] == ' ' or cont == 0:
            result += text[cont].upper()
        else:
            result += text[cont]
        cont += 1
    print(result)


capitalizer("hi how are you doing?")
