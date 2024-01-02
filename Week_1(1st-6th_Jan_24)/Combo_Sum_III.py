"216. Combination Sum III"
from itertools import combinations
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        num = list(range(1,10))
        
        for combo in combinations( num , k):
            if sum( combo ) == n:
                res.append(list(combo))
        return res
