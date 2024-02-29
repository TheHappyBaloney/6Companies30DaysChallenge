# 1686. Stone Game VI
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        val = zip( aliceValues , bobValues )
        val = sorted( val , key = lambda x: sum(x) , reverse = True )
        a = sum(i[0] for i in val[::2] )
        b = sum(j[1] for j in val[1::2] )
        if a > b:
            return 1
        elif b > a:
            return -1
        else:
            return 0
