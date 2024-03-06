# 2225. Find Players With Zero or One Losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer=[[],[]]
        d={}
        for i in matches:
            d[i[1]] = d.get(i[1],0)+1
            d[i[0]] = d.get(i[0],0)+0
        for j , k in d.items():
            if k == 0:
                answer[0].append(j)
            if k == 1:
                answer[1].append(j)
        answer[0].sort()
        answer[1].sort()
        return answer
