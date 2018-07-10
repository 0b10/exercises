"""
Jewels and stones
https://leetcode.com/problems/jewels-and-stones/description/
"""

'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''


class Solution:
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        num_of_jewels = 0

        jewels = set(jewels)

        for stone in stones:
            if stone in jewels:
                num_of_jewels += 1

        return num_of_jewels


def test(obj, jewels, stones, expected):
    assert obj.numJewelsInStones(jewels, stones) == expected

solution = Solution()

test(solution, "aA", "aAAbbbb", 3)
test(solution, "z", "ZZ", 0)
test(solution, "aAbBzU1", "aAAAbbb11op", 9)
test(solution, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "$", 0)
test(solution, "aaaBBB", "aB", 2)  # Test uniqueness of jewels string.


