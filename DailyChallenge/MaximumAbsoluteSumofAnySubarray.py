# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
 

# Example 1:

# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
# Example 2:

# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8


# Hints:
# 1. What if we asked for maximum sum, not absolute sum?
# 2. It's a standard problem that can be solved by Kadane's algorithm.
# 3. The key idea is the max absolute sum will be either the max sum or the min sum.
# 4. So just run kadane twice, once calculating the max sum and once calculating the min sum.

import unittest
from itertools import accumulate

# # Solution 1
# class Solution:
#     def maxAbsoluteSum(self, nums: List[int]) -> int:
#         mins = maxs = curm = curmi = nums[0]
        
#         for i in nums[1:]:
#             curm = max(i, curm + i)
#             maxs = max(maxs, curm)

#             curmi = min(i, curmi + i)
#             mins = min(mins, curmi)

#         return max(maxs, abs(mins))
    


# # Solution 2
# class Solution:
#     def maxAbsoluteSum(self, nums: list[int]) -> int:
#         prefix=[0]*(len(nums)+1)
#         for i in range(len(nums)):
#             prefix[i+1]=prefix[i]+nums[i]
        
#         return max(prefix)-min(prefix)
    
    
# Solution 3
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        # Compute the prefix sum using accumulate, with initial=0
        s = list(accumulate(nums, initial=0))
        
        # The result is the difference between the max and min of the prefix sum
        return max(s) - min(s)


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


class TestMaxAbsSum(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [2,-5,1,-4,3,-2]
        result = solution.maxAbsoluteSum(nums=nums)
        self.assertEqual(result, 8)

    def test_case_2(self):
        solution = Solution()
        nums = [1,-3,2,3,-4]
        result = solution.maxAbsoluteSum(nums=nums)
        self.assertEqual(result, 5)

    def test_case_3(self):
        solution = Solution()
        nums = [7904,6631,-6203,-9981,-3670,6341,-579,7975,-404,-4264,-3735,-6364,-4570,2720,-9379,5741,8748,-9109,4216,-5040,9644,819,-8761,8529,10,-3995,1678,-1434,-2218,3741,-2859,5829,-4774,9158,-1110,-8725,4107,-6622,8594,9590,-7847,-6099,9673,1117,-5228,-7775,-8067,-1652,-8914,-2371,9566,-2098,-3214,-589,2689,-3490,7702,-3796,9823,7496,-4996,-9083,5286,-8442,3781,-8534,-3996,-1546,-3997,5527,-6690,-4745,7956,-6792,-9915,2530,-6263,-5676,6810,791,-1545,-2658,-7439,5739,3990,285,-548,3663,828,6826,3080,-7243,-1294,6647,7492,7923,7000,-5557,4379,-7760,-3441,6129,4709,-5313,-874,6615,7316,2287,-2545,1933,6144,120,-7493,-6685,-5689,2952,-3717,4518,-9804,1293,-190,2534,9925,2037,-7267,8597,-4385,165,6152,2467,-8419,-5356,5364,9181,3212,-7947,9161,-4683,9646,6150,5928,2430,5921,-8212,-1452,-6634,5031,-7269,-605,1085,-4605,-8285,-1652,-4358,-9840,118,3133,9770,-7909,-3181,3865,4603,2549,8259,5017,-8668,9607,9705,-9441,-2709,-7725,3494,-223,-3800,-4535,-7426,7959,5988,4291,-3227,-9991,8437,5558,7947,6973,9632,7598,1973,-583,-1225,980,2115,2766,-8693,6925,-6299,-7785,876,7090,-6945,7121,-4189,9961,3200,-1065,7267,-5005,-7465,9541,5122,8920,5799,3276,-3436,-6706,3385,517,8629,-498,-2164,6475,4367,-9104,-6023,3838,580,-7839,7301,224,4845,-9113,-4450,-7537,-16,3042,4854,8024,3396,7529,-9133,3462,-5888,-9206,1773,8189,9837,6012,459,1520,9982,2334,-9795,1136,-6128,9439,-5198,2793,-9174,8905,7827,3068,7298,-2062,1342,-6348,-2142,-1414,-2351,7092,6140,-3230,-8197,4588,7251,2658,6799,5410,-40,7621,3229,800,7574,-2090,-7100,-2865,164,5365,6927,-3107,-8072,9036,4683,-522,2600,-7383,5457,-4278,-4937,3384,5339,3648,-376,2862,1962,-8571,-690,-3348,-7236,-7035,6144,-6032,-6104,1803,6754,396,-5835,-3659,-1457,5265,8903,6276,-8275,-7630,2174,3955,5989,2552,-5328,-8395,-834,8409,-2078,9519,705,-529,-8612,-9507,-6367,-841,2862,-3781,6503,-4098,-7794,3657,-9253,-4402,-5322,-7484,-6464,-7891,8580,9714,-2204,8050,5776,7412,4606,5665,4752,7491,903,195,-3152,2354,986,-5613,-4541,6873,-2945,6876,2071,5291,-5633,150,-4000,-336,9823,6203,8321,7801,-330,5732,-7610,-6064,8432,-6082,2224,6634,5310,7996,-7451,-826,-4271,-5588,24,-749,6658,3714,-5702,6706,8334,6197,-5970,8324,2493,-9490,-2214,1781,1699,-5895,2374,8675,-2608,-2458,-9262,-3691,-4215,-9773,-9030,-5358,3693,1027,4866,2301,-7587,5409,137,-922,-4308,4502,-974,8961,-8135,4618,-8152,-5205,-5821,9070,9144,-1943,-6248,-3851,2408,7594,-7525,-8964,-3781,8849,-2359,9234,-5986,-4869,-2134,-5472,-2347,-4850,-8976,-9943,-3187,-4238,1035,-3228,-8825,9384,7078,-5881,4794,-9705,2686,4319,-9885,6835,6173,9463,5029,-6217,-4521,-2302,230,-5381,5610,-9516,-4168,-5731,-4441,-2841,-2586,2843,9837,-903,-743,-7129,8794,792,-3970,5999,4875,-5223,-8971,-3787,3126,4047,3789,443,-4048,-34,-7872,6398,-9835,6525,2639,-4950,3263,9046,-6298,-2031,-8202,9069,5544,1022,-2853,2104,-4726,-2022,-6074,7052,9081,7478,-5355,-3511,4377,-581,9710,4272,2296,6175,3415,7498,-3844,-3915,1846,4722,5468,7175,8412,1788,3139,-7584,7258,-90,-3078,3178,-770,-8452,-9276,416,133,4996,-5388,-682,-1528,9914,-8280,7007,-6531,-5485,-2054,-7308,-2194,-7213,2578,259,-6349,-5378,9612,5631,7424,-9989,-4759,-6769,92,-3597,6327,1916,878,-6916,-2468,-9804,5100,9474,-5687,9603,-1629,-8516,-7324,-122,-1197,-8835,-5970,2883,8501,9305,2821,-7136,-4520,8387,-4559,8405,9268,-9331,2137,854,1628,4918,4381,411,9147,1507,-4358,-2434,1400,7115,-9093,7381,4862,-4343,9854,2844,-306,7273,-1814,9028,8378,5233,-8385,9916,-5185,-3973,-560,-1331,-9317,-1459,2891,-3883,3260,4045,7650,-8365,-9982,-5070,2114,-6751,-2469,-3153,-1396,3677,4192,-9793,5575,2922,5308,2700,7463,8277,3093,145,1097,5643,4690,1104,-9440,43,51,-2529,1608,7375,-3610,-5998,-1019,6779,5334,-2150,8761,7027,5218,-5867,4582,-833,-2152,2521,4461,-2929,4678,4612,-1250,8126,-3510,3375,8567,1053,5390,-265,-614,2599,3269,-4537,2304,1022,8597,-6995,-6231,9954,1201,-2703,-5101,-2544,-6812,2362,282,-6625,-3300,-682,161,7025,3281,5694,-9435,-1818,4885,-1191,4492,6133,5533,-4752,8168,-2467,8231,-4594,-1491,-2235,-934,9879,9277,6125,-860,-4007,3258,657,-3856,5594,-6408,7021,-4754,2053,-1365,-27,6272,355,228,4257,-6917,1636,8394,2490,6737,1166,2257,8959,5225,-7459,-8187,-5301,-7133,6831,3466,8931,-2928,3015,-8863,-8054,-700,2421,2879,2190,-5708,8597,-4001,4384,-340,5118,-6318,1232,-5296,2954,-759,-4799,6310,-1722,-3596,-8659,2108,3114,8838,-2495,-8466,5122,-1556,1491,-1948,-124,6881,-1365,-6104,4502,2221,-8384,3353,2472,7654,-5378,6326,2284,-5029,-9446,-9548,5946,-4094,8798,-4669,5938,-1968,-2368,-8414,-1241,-2138,-2659,1162,9852,-9721,8411,-828,2396,-1145,-9052,-3858,-4266,6889,1864,6978,-6816,-1408,-9501,-851,757,-1286,5922,-8438,-3443,-3582,-4674,7340,-1602,-2735,-9982,6673,-8873,6277,-9955,-6371,-8003,-8615,-1702,-510,3998,-3161,-3859,2659,-1431,-8355,1853,7695,3042,1274,-2716,-9749,-725,-7752,-6652,1620,-6926,-9630,-1450,-8702,-8021,-7035,6568,-7503,-7699,1781,8492,1412,620,-9130,4946,-6818,-2434,1488,7044,-9180,9383,7735,-7907,5043,-5241,5785,-6729,-2140,-4433,-3923,5079,7546,4091,4020,-3400,-7924,6651,-5255,7297,-9506,869,4358,-6805,-2539,-4833,-4306,-5388,-4010,-6571,80,2291,-523,5851,8306,-7719,206,-2473,6419,5532,-4369,9112,-2893,-2291,-5479,-9857,3592,6,3477,4667,3873,6751,7507,-4611,429,-8128,-1299,-4597,725,1860,-1180,-4414,8642,8041,6359,-873,7555,-3197,9442,9878,2441,-6070,2296,4003,-6027,9222,2908,160,5152,608,-8033,-5532,-3495,554,2060,4315,2961,-9886,-5308,8725,-9140]
        result = solution.maxAbsoluteSum(nums=nums)
        self.assertEqual(result, 344984)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())



# Explanation:
# Kadane's Algorithm is an efficient way to solve the maximum subarray sum problem. The problem is to find the contiguous subarray (within a given one-dimensional numeric array) which has the largest sum.

# Problem Definition:
# Given an integer array nums, you need to find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

# Kadane's Algorithm Explanation:
# Kadane’s algorithm works by iterating through the array and maintaining two variables:

# current_sum: Tracks the sum of the current subarray as we iterate through the array.
# max_sum: Tracks the maximum sum encountered so far.
# The idea is:

# For each element in the array, decide whether to:
# Add the element to the current subarray (current_sum), or
# Start a new subarray from this element.
# You choose the larger of these two options:

# If adding the current element to the subarray leads to a larger sum, keep adding.
# If starting a new subarray leads to a larger sum, reset the current sum to the current element.
# Algorithm Steps:
# Initialize:
# current_sum = 0
# max_sum = -infinity (or a very small number initially)
# Traverse the array, and for each element:
# Update current_sum: Take the maximum between the current element and the sum of current_sum + element.
# Update max_sum: Track the maximum of max_sum and current_sum.
# Return max_sum as the result.
# Time Complexity:
# Time Complexity: O(n), where n is the number of elements in the array. The algorithm makes just one pass through the array.
# Space Complexity: O(1), as it uses only a constant amount of space.




# Example Walkthrough:
# For nums = [2, -5, 1, -4, 3, -2], here’s how the code works:

# Calculate the prefix sum s: Using accumulate(nums, initial=0), we get:

# ini
# Copy
# s = [0, 2, -3, -2, -6, -3, -5]
# The initial=0 is added at the beginning, so s[0] = 0.
# Each subsequent value in s is the cumulative sum up to that index in the original nums array.
# Find the maximum and minimum values in s:

# max(s) = 2
# min(s) = -6
# Compute the result: The maximum absolute sum is max(s) - min(s) = 2 - (-6) = 8.

# Final Output:
# For the input [2, -5, 1, -4, 3, -2], the output is 8.