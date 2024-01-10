# 2002 : Maximum product of the length of two palindromic sequences 

class Solution:
    def maxProduct(self, s: str) -> int:
        n , pali = len(s) , {}
        res = 0
        
        for mask in range ( 1 , 1 << n ):
            subseq = ""

            for i in range (n):
                if mask & ( 1 << i ):
                    subseq += s[i]

            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)
                            
        for m1 in pali :
            for m2 in pali :
                if m1 & m2 == 0 :
                    res = max(res, pali[m1] * pali[m2])

        return res
