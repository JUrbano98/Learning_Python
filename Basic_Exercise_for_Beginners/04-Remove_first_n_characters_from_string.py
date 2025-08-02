'''
Write a Python code to remove characters from a string from 0 to n and
return a new string.
'''


def remove_chars(word, n):
    return (word[n:])


print(remove_chars("My name is Javier", 9))  # Expected: "s Javier"
