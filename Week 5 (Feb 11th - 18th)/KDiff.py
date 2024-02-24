# 532. K-diff Pairs in an Array

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        pairs = set()
        seen = set()

        for i in range(len(nums)):
            if nums[i] - k in seen:
                pairs.add((nums[i] - k, nums[i]))  
            seen.add(nums[i])  

        return len(pairs)
