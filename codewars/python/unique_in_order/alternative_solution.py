"""
A clever and concise solution to the Unique in Order problem on codewars.
http://www.codewars.com/kata/unique-in-order/python

All credit goes to user6270586, emma8463, and ItsAdi - here:
http://www.codewars.com/kata/reviews/54e659a9e323fec7c30002a7/groups/54e692677f087cf61000124e
"""


def unique_in_order(iterable):
    # If it's the first index, or it's not equal the one behind it, then return it
    return [z for i, z in enumerate(iterable) if i == 0 or iterable[i - 1] != z]


def test(iterable, expected_result):
    assert unique_in_order(iterable) == expected_result


test('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B'])
test('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D'])
test('A', ['A'])
test([1, 2, 2, 3, 3], [1, 2, 3])
