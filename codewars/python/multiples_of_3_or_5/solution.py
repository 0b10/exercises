"""
A solution for the Multiple of 3 or 5
http://www.codewars.com/kata/multiples-of-3-or-5/python
"""

'''
!! Description !!
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def solution(number):
    _sum = 0

    for factor in range(1, number):
        if (factor % 3 == 0) or (factor % 5 == 0):
            _sum += factor

    return _sum


def test(number, expected_result):
    assert solution(number) == expected_result

test(10, 23)
test(20, 78)
