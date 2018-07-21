"""
My solution to the 'Is My Friend Cheating' problem on codewars.
https://www.codewars.com/kata/is-my-friend-cheating/python
"""

'''
! Problem description

* A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
* Within that sequence, he chooses two numbers, a and b.
* He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
* Given a number n, could you tell me the numbers he excluded from the sequence?
* The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".

It happens that there are several possible (a, b). The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).

(See examples of returns for each language in "RUN SAMPLE TESTS")

Examples:

removNb(26) should return [(15, 21), (21, 15)]
or

removNb(26) should return { {15, 21}, {21, 15} }
or

removeNb(26) should return [[15, 21], [21, 15]]
or

removNb(26) should return [ {15, 21}, {21, 15} ]
or

removNb(26) should return "15 21, 21 15"
or

in C:
removNb(26) should return  **an array of pairs {{15, 21}{21, 15}}**
tested by way of strings.
'''

'''
! What I learned
* I need to brush up on my algebra.
* Problems like this can be solved in O(n) time with algebra, relative to a much more complex brute-force solution.
* Unittest is not sufficient. I will look at pytest. I was having issues with a test that was returning an empty list.
    Looping over the results and applying to forumla would always return true - which shouldn't be the case.
* Linters can have bugs. The pycharm built-in linter recognises b as an integer (within removeNB()) when it's a float.
'''

def get_b(a, sum_n):
    """
    Return the corresponding value (b), from (a), where a*b is equal to sum_ - a - b.
    :param a: The input that b is derived from.
    :param sum_n: The sum of the input range set: 1..n
    :return: b (Float), the corresponding value to a and sum_.
    """
    return (-a + sum_n) / (a + 1)


def removNb(n):
    """
    Given 'n', compute the sum for 'n', and find (a, b) where ab = sum - a - b.
    In other words, the product of ab must equal the sum of n, excluding a and b.
    :param n: The maximum number for the input problem space.
    :return: A List of tuples, containing result pairs.
    """
    sum_n = sum(range(1, n+1))
    result = []
    for a in range(1, n+1):
        b = get_b(a, sum_n)
        if b.is_integer() and b <= n:  # b is 100% float. Test it.
            result.append((a, int(b)))

    return result
