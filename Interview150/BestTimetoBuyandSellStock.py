# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


import unittest

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        profits = [0] * len(prices)
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            profits[i] = prices[i] - mini

        return max(profits)
        
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

class TestTimeToBuyStocks(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        prices = [7,1,5,3,6,4]
        result = solution.maxProfit(prices)
        self.assertEqual(result, 5)

    def test_case_2(self):
        solution = Solution()
        prices = [7,6,4,3,1]
        result = solution.maxProfit(prices)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)



# ### **Explanation:**

# 1. **Initialize Variables:**
#    - Create an array `profits` with the same length as `prices`, initialized to zero.
#    - Set the initial minimum price `mini` as `prices[0]` (the first price).

# 2. **Iterate Through Prices:**
#    - For each price `prices[i]`, update the `mini` variable to store the minimum price encountered so far by comparing `mini` with `prices[i]`.
#    - Calculate the profit at each day by subtracting `mini` from the current price `prices[i]`, and store the result in the `profits` array.

# 3. **Find the Maximum Profit:**
#    - After iterating through all prices, return the maximum value from the `profits` array, which represents the maximum possible profit.

