# PALINDROME PYTHON 3 PROGRAM.
# Created by Yerenzter

# Create a function for palindrome.
def palindrome(value):
    result = ""
    value = str(value)
    for values in range(len(value)):
        reverse=(len(value)-values)-1
        result+=value[reverse]

    if result == value:
        return f'{value} is a palindrome'
    else:
        return f'{value} is not a palindrome'
