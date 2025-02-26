# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

import unittest

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k%len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        # temp = nums[:]
        # l = len(nums)
        # for i in range(l):
        #     print(temp[(i + k)% l], (i + k)% l-1)
        #     nums[(i + k)% l] = temp[i]


class TestRotateArray(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        solution.rotate(nums,k)
        self.assertEqual(nums,[5, 6, 7, 1, 2, 3, 4])

    def test_case_2(self):
        solution = Solution()
        nums = [1, 3, 5, 7, 9, 11, 13]
        k = 4
        solution.rotate(nums,k)
        self.assertEqual(nums,[7, 9, 11, 13, 1, 3, 5])

if __name__ == '__main__':
    unittest.main()