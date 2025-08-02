'''
Given two lists of numbers, write Python code to create a new list containing
odd numbers from the first list and even numbers from the second list.
'''

def merge_special(str1, str2):
    result = []
    for i in str1:
        if i % 2 != 0:
            result.append(i)
    for j in str2:
        if j % 2 == 0:
            result.append(j)
    return result


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print(merge_special(list1, list2))
