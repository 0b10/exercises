"""
Reverse a given integer.
https://leetcode.com/problems/reverse-integer/description/
"""

'''
!! Problem Description !!

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
overflows.
'''

'''
Challenges I faced:
    * The answer must be within a 32 bit signed integer range. Python supports integers much larger than this by default.
    * That a number within that range, when reversed, can be outwith it. This threw me off initially.
    * After I had established that fact, I had to determine what the maximum value would be - which would be less than
    (2^32)-1 and greater than it's negated compliment. As it turned out, a 'palindrome' was the answer. A number that is
    the same when reversed turns out to the the boundary for the solution space - otherwise such solutions would have to
    either violate the max input value, or the max output value.
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if (x < -2147483648) or (x > 2147483647):  # Input must be a 32bit unsigned integer.
            return 0

        negative_num = False

        if x < 0:  # Detect negation
            x *= -1
            negative_num = True

        num_string = str(x)[::-1]  # Reverse it.
        x = int(num_string)

        if negative_num:
            x *= -1

        if (x < -2147483648) or (x > 2147483647):  # Output must be a 32bit unsigned integer.
            return 0

        return x


solution = Solution()

# !! Simple tests !!
assert solution.reverse(123) == 321
assert solution.reverse(-123) == -321
assert solution.reverse(120) == 21
assert solution.reverse(100) == 1
assert solution.reverse(0) == 0
assert solution.reverse(1534236469) == 0


# !! Boundary testing !!
# Min 32bit unsigned int.
assert solution.reverse(-2147483647) == 0
assert solution.reverse(-2147483648) == 0
assert solution.reverse(-2147483649) == 0

# Max 32bit unsigned int.
assert solution.reverse(2147483646) == 0
assert solution.reverse(2147483647) == 0
assert solution.reverse(2147483648) == 0

# Max acceptable number when reversed.
assert solution.reverse(2147447411) == 1147447412
assert solution.reverse(2147447412) == 2147447412
assert solution.reverse(2147447413) == 0

# Min acceptable number when reversed.
assert solution.reverse(-2147447411) == -1147447412
assert solution.reverse(-2147447412) == -2147447412
assert solution.reverse(-2147447413) == 0
