# 1030. Matrix Cells in Distance Order

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res=[]
        for r in range(rows):
            for c in range(cols):
                res.append([r,c])
                
        res.sort(key=lambda x:abs(x[0]-rCenter)+ abs(x[1]-cCenter))
        return res
