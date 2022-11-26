'''
Write a function that takes a list value as an argument and
returns a string with all the items separated by a comma and a space,
with "and" inserted before the last item.
'''

def comma_code(list_val: list) -> str:

    result = ""
    for i in range(len(list_val)):
        if i < len(list_val) - 1:
            result += list_val[i] + ", "
        else:
            result += "and " + list_val[i]
    
    return result

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))