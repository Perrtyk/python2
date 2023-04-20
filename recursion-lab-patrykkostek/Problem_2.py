# Patryk Kostek
# Lab 2 Problem 2
"""
Using the PyCharm provided in the starting files as a starting point, write a recursive function to calculate the nth
fibonacci number and use it to write an application that displays the first 10 fibonacci numbers.  The function should
take an integer n as its parameter and return an integer.

In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that
each number is the sum of the two preceding ones, starting from 0 and 1. That is,{\displaystyle F_{0}=0,\quad F_{1}=1,}
and {\displaystyle F_{n}=F_{n-1}+F_{n-2},} for n > 1. The beginning of the sequence is thus:

{\displaystyle 0,\;1,\;1,\;2,\;3,\;5,\;8,\;13,\;21,\;34,\;55,\;89,\;144,\;\ldots }
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main(n):
    fibonacci_list = []
    for i in range(n):
        fibonacci_list.append(fibonacci(i))
        print(f"F_{i}     {fibonacci_list[i]}")


if __name__ == '__main__':
    main(10)


# The main issues I faced with this problem was the recursion error of n == 1. I initially set the base case as n == 1
# and was unsure how to solve it properly for the recursion to work. After wednesday's class, I was able to understand
# why and how this impacts the running of the code. If we start with 0, go on to 1, it seemed to be stuck in an infinity
# loop. To solve this, I learned that n <= 1 is the proper base case for the fibonacci program.


