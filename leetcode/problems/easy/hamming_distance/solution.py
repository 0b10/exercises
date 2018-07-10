"""
Return the hamming distance between two integers.
https://leetcode.com/problems/hamming-distance/description/
"""

'''
What I learned from this:
    * That ^ is the XOR operator
    * That 0b is binary notation, and yields an integer: type(0b1111) is <class 'int'>
    * That bin(x) yields a binary string (string type)
    * Binary literals are defined without quotations, yes, this should be obvious
    * That there's no unsigned int type, but they can be represented in binary with some black magic.
'''


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        xored_int = x ^ y
        return bin(xored_int).count('1')


def test_bins(obj, bin1, bin2, expected_bin_result):
    assert obj.hammingDistance(bin1, bin2) == expected_bin_result


def test_ints(obj, int1, int2, expected_int_result):
    assert obj.hammingDistance(int1, int2) == expected_int_result


solution = Solution()

# !! Tests !!
# integers
test_ints(solution, 1, 4, 2)
test_ints(solution, 0, 0, 0)
test_ints(solution, 0, 1, 1)
test_ints(solution, 0, 2147483647, 31)

# Binary
test_bins(solution, 0b1111, 0b0000, 4)
test_bins(solution, 0b1101011, 0b0100101, 4)
# Test 32 bit boundary
test_bins(solution, 0b0000000000000000000000000000001, 0b0000000000000000000000000000000, 1)  # 31 bit.
test_bins(solution, 0b00000000000000000000000000000011, 0b00000000000000000000000000000001, 1)  # 32 bit.
test_bins(solution, 0b000000000000000000000000000000011, 0b000000000000000000000000000000001, 1)  # 33 bit.
