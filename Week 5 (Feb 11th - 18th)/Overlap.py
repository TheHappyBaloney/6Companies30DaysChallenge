# 1401. Circle and Rectangle Overlapping

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        X = max( x1 , min( x2 , xCenter ) )
        Y = max( y1 , min( y2 , yCenter ) )

        dist_x = X - xCenter
        dist_y = Y - yCenter

        pyth = ( dist_x ** 2 ) + ( dist_y ** 2 )
        rad = (radius ** 2)
        
        return pyth <= rad
