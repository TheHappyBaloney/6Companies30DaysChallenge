from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        lis = [envelopes[0][1]]

        for i in range(1, n):
            if envelopes[i][1] > lis[-1]:
                lis.append(envelopes[i][1])
            else:
                left, right = 0, len(lis) - 1
                while left < right:
                    mid = (left + right) // 2
                    if lis[mid] < envelopes[i][1]:
                        left = mid + 1
                    else:
                        right = mid
                lis[left] = envelopes[i][1]

        return len(lis)

