# 4)  Write a program which returns a boolean value indicating whether a given sentence is a palindrome.  A sentence
# which contains the same character sequence when reversed (ignoring whitespace).
# Example: "step on no pets" or "put it up".

def is_palindrome(string_in):
    string_in = string_in.replace(" ", "")
    reversed_string = string_in[::-1]
    if string_in == reversed_string:
        return True
    else:
        return False


print(is_palindrome("put it up"))
print(is_palindrome("step on no pets"))

# Deleted or replaced the whitespaces with the .replace()
# Reversed the string the easiest way
# Then compared in the conditions of an if-else statement
# Then returned True or False accordingly.
