# 587. Erect The Fence

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def clockwise( a ,  b , c ):
            x1 , y1 = a
            x2 , y2 = b
            x3 , y3 = c

            return ( ( y3 - y2 ) * ( x2 - x1 ) - ( y2 - y1 ) * ( x3 - x2 ) )
        trees.sort()
        upper = []
        lower = []
        for t in trees:
            while len(upper) > 1 and clockwise( upper[-2] , upper[-1] , t ) > 0 :
                upper.pop()
            while len(lower) > 1 and clockwise( lower[-2] , lower[-1] , t ) < 0 :
                lower.pop()
            upper.append(tuple(t))
            lower.append(tuple(t))

        return list(set( upper + lower ))
