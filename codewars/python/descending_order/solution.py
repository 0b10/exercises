"""
A solution for the Descending Order problem on codewars,
http://www.codewars.com/kata/descending-order/python
"""

'''
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in
descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:

Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
'''


def Descending_Order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))


def test(num, result_expected):
    assert Descending_Order(num) == result_expected

test(1234567, 7654321)
test(217689403, 987643210)
test(112233994455667788, 998877665544332211)
