# 1227. Airplane Seat Assignment Probability

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n <= 1 :
            ans = 1 / n
        else :
            ans = 0.5
        return ans
