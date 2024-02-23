# 718. Maximum Length of Repeated Subarray

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        
        max_length = 0  
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1  
                    max_length = max(max_length, dp[i][j])  
        
        return max_length
