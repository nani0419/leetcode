
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

import unittest

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        l = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[l-2]:
                nums[l] = nums[i]
                l += 1
        # print(nums)
        # print(l)
        return l
    
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = len(nums)
#         count = 1
#         if l <= 2:
#             return l
#         cv = 0
#         for i in range(1,l):
#             if nums[i] == nums[i-1]:
#                 count += 1
#                 if count <= 2:
#                     cv += 1
#                     nums[cv] = nums[i]
#             else:
#                 count = 1
#                 cv += 1
#                 nums[cv] = nums[i]
#         return cv + 1



# numbers = [1, 1, 1, 2, 3, 3, 3, 3, 4, 4, 5]
# a = Solution()
# a.removeDuplicates(numbers)




# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         l = 2
#         for i in range(2, len(nums)):
#             if nums[i] != nums[l-2]:
#                 nums[l] = nums[i]
#                 l += 1
#         print(nums)  # This will print the modified array
#         print(l)  # This will print the length of the modified array
#         return l


class TestRemoveDuplicates(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums[:result], [1, 2, 3, 4, 5])

    def test_case_2(self):
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums[:result], [1, 1, 2, 2, 3])

    def test_case_3(self):
        solution = Solution()
        nums = [1, 1, 1, 1, 1]
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 2)
        self.assertEqual(nums[:result], [1, 1])

    def test_case_4(self):
        solution = Solution()
        nums = []
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 0)
        self.assertEqual(nums, [])

    def test_case_5(self):
        solution = Solution()
        nums = [1]
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 1)
        self.assertEqual(nums[:result], [1])

    def test_case_6(self):
        solution = Solution()
        nums = [3, 3, 3, 3, 3, 4, 4, 4]
        result = solution.removeDuplicates(nums)
        self.assertEqual(result, 4)
        self.assertEqual(nums[:result], [3, 3, 4, 4])


if __name__ == '__main__':
    unittest.main()
