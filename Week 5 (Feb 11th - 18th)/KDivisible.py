# 2261. K-Divisible Elements Subarrays 

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        sub = set()
        n = len(nums)
        for i in range(n):
            count = 0
            a = [ ]

            for j in range( i , n ):
                if nums[j] % p == 0:
                    count += 1 
                if count > k :
                    break
                a.append(nums[j])
                sub.add(tuple(a)) 
        return len(sub)
        
