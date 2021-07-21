# 1)  Write a program which prints the first n Fibonacci numbers. The first two numbers in the Fibonacci sequence are
# either 1 and 1, or 0 and 1, depending on the chosen starting point of the sequence, and each subsequent number is the
# sum of the previous two.
# Output: 0,1,1,2,3,5,8,13,21,34,55,89,144...

def fibonacci(n):
    if n >= 0:
        a = 0
        b = 1

        if n == 1:
            print(a)

        else:
            print(a)
            print(b)

            for i in range(2, n):
                temp = a + b
                a = b
                b = temp
                print(temp)

    else:
        print("No negative numbers")


fibonacci(10)

# https://github.com/navinreddy20/Python-/blob/master/41%20Fibonacci%20Sequence.txt
# Got the inspiration from the link above.
# Can be sorted with recursion but choose to use "Space optimised" version.
# Reasoning: It's pretty elegant and easy to understand.
# Recursion can be hard to get your head around it at first.
