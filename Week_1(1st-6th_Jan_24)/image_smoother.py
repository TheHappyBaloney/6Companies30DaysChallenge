class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r = len(img)
        c = len(img[0])

        result = [[0]*c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                total = 0
                count = 0

                for a in range(max( 0 , i - 1 ) , min( r , i + 2 )):
                    for b in range(max( 0 , j - 1 ), min( c , j + 2)):
                        total += img[a][b]
                        count += 1

                result[i][j] = total // count

        return result 
