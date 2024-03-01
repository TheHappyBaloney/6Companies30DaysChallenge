# 1385. Find the Distance Value Between Two Arrays
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in range (len(arr1)):
            for j in range (len(arr2)):
                if abs( arr1[i] - arr2[j] ) <= d:
                    count += 1
                    break

        total = len(arr1) - count

        return total
