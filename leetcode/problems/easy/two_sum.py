"""
A solution for the Two Sum problem on LeetCode.com
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
        """
        Search a dict for the difference between the target, and each number in the list. Return the indices if found.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        _dict = {num: num for num in nums}

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if _dict.__contains__(difference):
                j = nums.index(difference)  # Get second index.

                if i != j:  # Can't be the same index.
                    return [i, j]


solution = Solution()

result = solution.twoSum([2, 7, 11, 15], 9)
print(result)
assert result == [0, 1]

result = solution.twoSum([3, 2, 4], 6)
print(result)
assert result == [1, 2]
