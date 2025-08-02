'''
Write a Python code to find how often the substring “Emma” appears
in the given string.
'''


def count_Emmas(str):
    return str.count("Emma")


string = "Emma is good developer. Emma is a writer"
print("Emma appears a total of", count_Emmas(string), "times.")  # Expected 2
