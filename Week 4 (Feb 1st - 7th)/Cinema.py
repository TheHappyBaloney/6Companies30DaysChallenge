# 1386. Cinema Seat Allocation

from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reversedSeatRowToSet = defaultdict(set)

        for row, col in reservedSeats:
            reversedSeatRowToSet[row].add(col)

        # we can create max 2 allocation from rows where there’s no reservation
        totalAllocation = 2 * (n - len(reversedSeatRowToSet))

        for reversedColSet in reversedSeatRowToSet.values():
            left, middle, right = False, False, False

            if 2 not in reversedColSet\
                and 3 not in reversedColSet\
                and 4 not in reversedColSet\
                and 5 not in reversedColSet:
                left = True

            if 4 not in reversedColSet\
                and 5 not in reversedColSet\
                and 6 not in reversedColSet\
                and 7 not in reversedColSet:
                middle = True

            if 6 not in reversedColSet\
                and 7 not in reversedColSet\
                and 8 not in reversedColSet\
                and 9 not in reversedColSet:
                right = True

            if left and right:
                totalAllocation += 2
            elif left or right or middle:
                totalAllocation += 1

        return totalAllocation
