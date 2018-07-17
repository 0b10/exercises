import re
"""
My solution to the 'Simple Pig Latin' problem on codewars.
https://www.codewars.com/kata/simple-pig-latin/python
"""

'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
untouched.

Examples:
    > pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    > pig_it('Hello world !')     # elloHay orldWay !
'''


def pig_it(sentence):
    words = re.split('(\W+)', sentence)

    for i, word in enumerate(words):
        words[i] = word[1:] + word[0] + 'ay' if word.isalpha() else word

    return ''.join(words)
