# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        rmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        intVal = 0

        for i in range(len(s)-1,-1,-1):
            cv = rmap[s[i]]

            if intVal == 0:
                intVal = cv
            elif cv >= rmap[s[i+1]]:
                intVal += cv
            else:
                intVal -= cv

        return intVal


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


class TestRomanToInteger(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        s = "MCMXCIV"
        result = solution.romanToInt(s)
        self.assertEqual(result, 1994)

    def test_case_2(self):
        solution = Solution()
        s = "LVIII"
        result = solution.romanToInt(s)
        self.assertEqual(result, 58)

    def test_case_3(self):
        solution = Solution()
        s = "III"
        result = solution.romanToInt(s)
        self.assertEqual(result, 3)
        

if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)

