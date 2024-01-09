# 462. Minimum Moves To Equal Array Elements  

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        s = sorted(nums)
        m = s[len(s)//2]
        c = 0
        for i in s:
            if i == m:
                continue
            else:
                c += abs( i - m )
        return c
