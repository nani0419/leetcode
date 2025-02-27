# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

import unittest

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        jump = nums[0]
        i = 1
        while (jump > 0) & (i < len(nums)):
            jump = max(jump-1,nums[i])
            i += 1

        return i == len(nums)
    
class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"\n{test._testMethodName}: Pass")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"\n{test._testMethodName}: Fail")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"\n{test._testMethodName}: Error")


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult

class TestJumpGame(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [2,3,1,1,4]
        result = solution.canJump(nums)
        self.assertEqual(result, True)
    
    def test_case_2(self):
        solution = Solution()
        nums = [3,2,1,0,4]
        result = solution.canJump(nums)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)