# Patryk Kostek
# Lab 2 Problem 3

"""

Using the PyCharm project provided in the starting files as a starting point, write a recursive function to determine if
a string is a palindrome.  The function should take a string s as its parameter and return a bool. Use your function to
write an application that asks the user to enter a word or phrase from the keyboard and then tells the user whether or
not the text that they entered is a palindrome.  Capitalization whitespace and punctuation should be removed before
calling your function.
A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward,
such as madam, racecar.

"""

def palindrome(s):
    if len(s) == 0:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        return False

def main():
    print('Welcome to the Palindrome Word Tester. . .\n')
    userInput = input('Word to Test: ').lower()
    cleanedString = ''
    for char in userInput:
        if char in "abcdefghijklmnopqrstuvwxyz":
            cleanedString += char
    print(cleanedString)
    is_palindrome = palindrome(cleanedString)
    if is_palindrome:
        print(f"Yes, '{userInput}' is a palindrome.")
    else:
        print(f"No, '{userInput}' is not a palindrome.")


if __name__ == '__main__':
    main()

# This problem, I did not have many issues except for the string being printed out twice. I found that it was due to me
# not separating the cleaned string and input string. After adjusting the variables, I was able to get the palindrome
# program running as expected.