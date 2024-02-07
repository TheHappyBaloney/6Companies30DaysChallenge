# 396. Rotate Function
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        s = sum(nums)
        for i in range (0 , n):
            ans += (i * nums[i])
        m = ans
        for i in range( 1 , n ):
            ans += s - n * nums[n - i]
            m = max(m,ans)
        
        return m 
