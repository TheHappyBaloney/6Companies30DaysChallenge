# 1334. Find the city with the smallest no. of neighbours at a threshold distance

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj={i:dict() for i in range(n)}
        for u,v,d in edges:
            adj[u][v]=d
            adj[v][u]=d
        cities=[0]*n
        for k in range(n):
            c=-1
            dist=[float('inf')]*n
            dist[k]=0
            visited=[0]*n
            pq=[(0,k)]
            heapify(pq)
            while pq:
                d,node=heappop(pq)
                if d>distanceThreshold:
                    break
                if visited[node]:
                    continue
                visited[node]=1
                c+=1
                for v in adj[node]:
                    if visited[v]==0 and d+adj[node][v]<dist[v]:
                        dist[v]=d+adj[node][v]
                        heappush(pq,(dist[v],v))
            cities[k]=c
        maxNode=0
        minDist=cities[0]
        for i in range(n):
            if cities[i]<=minDist and maxNode<i:
                maxNode=i
                minDist=cities[i]
        return maxNode    
