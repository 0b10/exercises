"""
My horrible solution to the Unique in Order problem on codewars.
http://www.codewars.com/kata/unique-in-order/python
"""

'''
This is an awful, hacky, unreadable solution.

What I learned from this:
    * That one-line if, else, statements are possible, with multiple clauses
    * That accessing an index out of bounds actually seems to trigger an else clause when using the one line solution.
        More research is needed on this.
'''


def get_unique(i, value, iterable):
    return value if i == 0 or value != iterable[i-1] else None


def unique_in_order(iterable):
    return list(filter(None, [get_unique(i, value, iterable) for i, value in enumerate(iterable)]))


def test(iterable, expected_result):
    assert unique_in_order(iterable) == expected_result


test('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B'])
test('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D'])
test('A', ['A'])
test([1, 2, 2, 3, 3], [1, 2, 3])
