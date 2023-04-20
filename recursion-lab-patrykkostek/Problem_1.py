# Patryk Kostek
# Lab 2 Problem 1

"""
Using the PyCharm project provided in the starting files as a starting point, write a recursive function to calculate
the nth triangular number and use it to write an application that displays the first 10 triangular numbers.  The
function should take an integer n as its parameter and return an integer.

The triangular number T_1 is a figurate number that can be represented in the form of a triangular grid of points where
the first row contains a single element and each subsequent row contains one more element than the previous one. This is
illustrated above for T_1=1, T_2=3, .... The triangular numbers are therefore 1, 1+2, 1+2+3, 1+2+3+4, ..., so for n=1, 2,
..., the first few are 1, 3, 6, 10, 15, 21,
"""

def triangulation(n):
    if n == 1:
        return n
    else:
        return n + triangulation(n - 1)


def main():
    for i in range(1, 21):
        print("T_{:<2}    {:3}".format(i, triangulation(i)))


if __name__ == '__main__':
    main()


# I initially stuggled with the understanding of recursion. This was a great first problem as it is not too difficult
# to grasp. I mainly had issues with the call of the function and was having a hard time understanding how recursion works
# as a whole. Working through this problem slowly made it easier to understand.