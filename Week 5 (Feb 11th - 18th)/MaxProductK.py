# 2233. Max Product after K increment

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        res = 1
        n = 10 ** 9 + 7
        heapify( nums )
        while ( k != 0 ):
            a = heappop( nums )
            heappush( nums , a + 1 )
            k -= 1
        for i in nums:
            res=(res*i)%n
        return res
