# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.


# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
import unittest

class Solution:
    def candy(self, ratings: list[int]) -> int:
        l = len(ratings)
        cand = [1] * l
        i = 1
        while i < l:
            if ratings[i] > ratings[i-1]:
                cand[i] = cand[i-1] + 1
            i = i + 1

        i = l-2
        while i >= 0:
            if ratings[i] > ratings[i+1]:
                cand[i] = max(cand[i],cand[i+1] + 1)
            i = i - 1

        return sum(cand)


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


class TestCandy(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        rating = [1,2,2]
        result = solution.candy(rating)
        self.assertEqual(result, 4)

    def test_case_2(self):
        solution = Solution()
        rating = [1,0,2]
        result = solution.candy(rating)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner)
