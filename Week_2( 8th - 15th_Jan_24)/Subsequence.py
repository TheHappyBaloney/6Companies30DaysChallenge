#2099. Find the subsequence of length k with the largest sum

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        heapq.heapify(pq)
        for i in range (len(nums)):
            heapq.heappush(pq,[nums[i], i])
            if ( len(pq) > k ):
                heapq.heappop(pq)
        
        pq.sort( key = lambda x : x[1] )
        ans = []
        for i in range (len(pq)):
            ans.append(pq[i][0])
        return ans 
