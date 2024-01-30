# 455. Assign cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        j = 0 
        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1

            if j >= len(s):
                return i

            j += 1

        return len(g)
