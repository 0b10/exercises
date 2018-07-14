from itertools import groupby

"""
A more elegant solution to the Unique in Order problem on codewars.
http://www.codewars.com/kata/unique-in-order/python
"""

'''
What I learned from this:
    * groupby() preserves order: AABBCCAA => ABCA
    * Keys are unique consecutive items: AABBCCAA => ABCA
    * Groups are consecutive items grouped up: AABBCCAA => AA BB CC AA
'''


def unique_in_order(iterable):
    return [key for key, _ in groupby(iterable)]


def test(iterable, expected_result):
    assert unique_in_order(iterable) == expected_result


test('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B'])
test('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D'])
test('A', ['A'])
test([1, 2, 2, 3, 3], [1, 2, 3])
