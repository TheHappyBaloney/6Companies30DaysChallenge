#1248. Count no. of nice subarrays

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 
        
        odd_count = 0
        result = 0
        
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            
            if odd_count - k in prefix_count:
                result += prefix_count[odd_count - k]
            
            prefix_count[odd_count] += 1
        
        return result
