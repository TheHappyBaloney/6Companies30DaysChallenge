# 2343. Query Kth Smallest Trimmed Number
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []
        for x,y in queries:
            li = []
            heapq.heapify(li)
            for i in range(len(nums)):
                
                n1 = nums[i][len(nums[i])-y:len(nums[i])]
                n1 = int(n1)
                
                if len(li) < x:
                    heapq.heappush(li,[-1*n1,-1*i])
                
                else:
                    if n1<-1*li[0][0]:
                        heapq.heappop(li)
                        heapq.heappush(li,[-1*n1,-1*i])
               
            answer.append(-1*heapq.heappop(li)[1])       
        return answer
                
