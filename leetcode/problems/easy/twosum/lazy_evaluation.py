"""
An alternative solution for the Two Sum problem on LeetCode.com
This code was not written by me, and credit is given to wanglouis49:
    https://leetcode.com/wanglouis49/
    https://leetcode.com/problems/two-sum/discuss/144554/Python-concise-O(n)-solution/152756

"""

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        mem = dict()  # Uninitialised, lazy evaluation. The last statement of the method stores key:value pairs it.

        for i, n in enumerate(nums):  # Gets (index, value) from enumeration(nums), and unpack it with tuple unpacking: e.g.  ' i, n '.
            if target - n in mem:  # Lazy evaluation. Each loop stores a value, and its index in the dict. Check to see if it's there.
                return [mem[target - n], i]  # If it's there, return the index of the value, and the current iteration
            mem[n] = i  # This is where the assignment, from the lazy evaluation occurs. Store {value, index}


solution = Solution()

result = solution.twoSum([2, 7, 11, 15], 9)
print(result)
assert result == [0, 1]

result = solution.twoSum([3, 2, 4], 6)
print(result)
assert result == [1, 2]
