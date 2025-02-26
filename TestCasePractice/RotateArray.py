import unittest

class Solution:
    def rotate(self, nums, k):
        # Rotate the array to the right by k steps
        k = k % len(nums)  # Handle case where k is larger than len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f'{test._testMethodName}: Pass')

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f'{test._testMethodName}: Fail')

    def addError(self, test, err):
        super().addError(test, err)
        print(f'{test._testMethodName}: Error')

class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult

class TestRotateArray(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        solution.rotate(nums, k)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_case_2(self):
        solution = Solution()
        nums = [1, 3, 5, 7, 9, 11, 13]
        k = 4
        solution.rotate(nums, k)
        self.assertEqual(nums, [7, 9, 11, 13, 1, 2, 5])

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
