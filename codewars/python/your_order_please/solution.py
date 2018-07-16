import re
"""
My solution to the 'Your order, please' problem on codewars.
https://www.codewars.com/kata/your-order-please/python
"""

'''
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position
the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive
numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

    > your_order("is2 Thi1s T4est 3a")
    > [1] "Thi1s is2 3a T4est"
'''

'''
What I learned from this
    * I was introduced to Python's regex:
        * regex functions can return a match object, which have their own methods for accessing data and/or groups.
    * Groups, in regex, express an order of precedence. They are also treated separately, and are returned as their
        own group in the result.
    * Not to over engineer solutions. I tried to account for float numbers within the solution - unnecessary. A simple
        /[1-9]+[0-9]/ would have sufficed. The filter() function could have been used for this, I have seen solutions
        doing so, but they don't account for 0 - the problem statement specifically outlined that 0 should not be
        considered as a primary digit:
            > "Numbers can be from 1 to 9. So 1 will be the first word (not 0)"
        which I'm assuming doesn't count '101'.
    * One-liners look ugly.
    * Lots of tests for one line of code.
'''


def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda s: re.search(r'([1-9]+[0-9]*)(\.[0-9]*)?', s).group()))
