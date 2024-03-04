# 2976. Minimum Cost to Convert String I

class Solution:
    def find(self, graph, x, y, d):
        if (x, y) in d:
            return d[(x, y)]
        pq, visit = [], set()
        heapq.heappush(pq, (0, x))
        while pq:
            cost, node = heapq.heappop(pq)
            if node == y:
                return cost
            if node in visit:
                continue
            visit.add(node)
            for nei, new_cost in graph[node]:
                heapq.heappush(pq, (cost+new_cost, nei))                  
        return -1
            
    
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        graph = collections.defaultdict(list)
        for x,y,z in zip(original, changed, cost):
            graph[x].append([y, z])
        
        res, d = 0, {}
        for i in range(n):
            val = self.find(graph, source[i], target[i], d)
            if val == -1:
                return -1
            else:
                res += val
            d[(source[i], target[i])] = val
        
        return res
