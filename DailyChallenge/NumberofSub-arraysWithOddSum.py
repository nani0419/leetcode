class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odds = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if sum(arr[i:j+1])%2 == 1:
                    odds += 1
        return odds

ar = [1, 3, 5]
sol = Solution()
print(sol.numOfSubarrays(ar))