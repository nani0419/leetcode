# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

import unittest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if all(s == "" for s in strs):
            return result
        strs.sort()
        fir,lst = strs[0],strs[-1]
        if fir == lst:
            return fir
        for i in range(min(len(fir),len(lst))):
            if fir[i] != lst[i]:
                return fir[:i]
            else:
                result = fir[:i+1]
        return result


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

class TestLongestCommonPrefix(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        strs = ["flower","flow","flight"]
        result = solution.longestCommonPrefix(strs)
        self.assertEqual(result, 'fl')

    def test_case_2(self):
        solution = Solution()
        strs = ["dog","racecar","car"]
        result = solution.longestCommonPrefix(strs)
        self.assertEqual(result, '')

    def test_case_3(self):
        solution = Solution()
        strs = [""]
        result = solution.longestCommonPrefix(strs)
        self.assertEqual(result, '')

    def test_case_4(self):
        solution = Solution()
        strs = ["a"]
        result = solution.longestCommonPrefix(strs)
        self.assertEqual(result, 'a')

if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)