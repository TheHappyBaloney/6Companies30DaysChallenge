# 368.Largest Divisible Subset

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [ [n] for n in nums ]
        sub = [nums[0]]
        for i in range ( len(nums) ):
            for j in range ( i ):
                if ( nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1):
                    dp[i] = dp[j] + [nums[i]]
                    if len(dp[i]) > len(sub):
                        sub = dp[i]

        return sub
