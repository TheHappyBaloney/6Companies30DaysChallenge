#451. Sort Characters by Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        st = ""
        for i in sorted(dic.items(), key=lambda x:x[1]):
            st += i[0] * i[1]
        return st[::-1]
        
