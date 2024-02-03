# 2970. Count the Number of Incremovable Subarrays I

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count=0
        for left in range(len(nums)):
            for right in range(left,len(nums)):
                A=nums[0:left]+nums[right+1:]
                valid=True
                for k in range(len(A)-1):
                    if A[k]<A[k+1]:
                        valid=True
                    else:
                        valid=False
                        break
                if valid:
                    count+=1
        return count
                
            
