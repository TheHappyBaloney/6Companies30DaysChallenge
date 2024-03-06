# 218. The Skyline Problem

from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        a = collections.defaultdict(list)
        ans = []
        last_height = 0
        for left, right, height in buildings:
            a[left].append((-1 , height))
            a[right].append((1 , height))
            
        sl = SortedList() 
        sl.add(0)
            
        for x in sorted( a.keys() ):
            for t , h  in a[x]:
                if t == -1:
                    sl.add(h)
                else:
                    sl.remove(h)

            curr_height = sl[-1]
            if curr_height != last_height:
                ans.append(( x , curr_height))
            last_height = curr_height
                
        return ans
