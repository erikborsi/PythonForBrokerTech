# 2)  Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the
# number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five
# print “FizzBuzz”.

def print_numbers_from_a_to_b(a, b):
    fizz = "Fizz"
    buzz = "Buzz"

    for i in range(a, b):
        if i % 3 == 0 and i % 5 == 0:
            print(fizz + buzz)
        elif i % 3 == 0:
            print(fizz)
        elif i % 5 == 0:
            print(buzz)
        else:
            print(i)


print_numbers_from_a_to_b(1, 101)

# Used the modulo operator to check if the reminder is 0.
# If the number can be divided by 3 and 5 it prints FizzBuzz.
# If the number can be divided by 3 it prints Fizz.
# If the number can be divided by 5 it prints Buzz.
# Range not includes the last specified number.
# For that reason when the function called, 101 need to be passed in the argument.
# Enclosed the strings into variables, to easily manipulate them if needed in the future.
