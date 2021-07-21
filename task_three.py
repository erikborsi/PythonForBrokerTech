# 3)  Write a program that given a string reverses each pair of characters and returns the result. If the string
# contains an uneven number of elements the last character should remain in place.
# Example: `John Smith` -> `oJnhS imht`
# Example: `Larry` => `aLrry`

def check_if_even(string_in):
    string_out = string_in

    if len(string_in) % 2 == 0:
        even(string_out)
    else:
        uneven(string_out)


def even(string_in):
    temp_list = []
    temp_list2 = []

    for i in string_in:
        temp_list.append(i)

    for j in string_in[0:len(string_in):2]:
        temp_list2.append(j)
        temp_list.remove(j)


    print(temp_list)
    print(temp_list2)

def uneven(string_in):
    print("uneven")


check_if_even("John Smith")
