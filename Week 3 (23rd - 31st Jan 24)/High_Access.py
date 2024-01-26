#2933. High Access Employee

class Solution:
    def time(self, t):
        return int(t[:2],10) * 60 + int(t[2:],10)
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        data = defaultdict(deque)
        res = set()
        acc = sorted(access_times, key = lambda x : x[1])
        for i , j in acc:
            data[i].append(self.time(j))
            while data[i][-1] - data[i][0] >= 60:
                data[i].popleft()
            if len(data[i]) >= 3:
                res.add(i)

        return list(res)
         
            
