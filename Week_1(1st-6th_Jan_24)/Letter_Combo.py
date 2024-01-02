# 17. Letter Combinations of a phone number

from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        numalpha = { '2' : ('a','b','c'), 
                     '3' : ('d','e','f'), 
                     '4' : ('g','h','i'), 
                     '5' : ('j','k','l'), 
                     '6' : ('m','n','o'), 
                     '7' : ('p','q','r','s'), 
                     '8' : ('t','u','v'), 
                     '9' : ('w','x','y','z'),
                     '0' : (' ')}
        dig = [numalpha[i] for i in digits]
        res = [''.join(combo) for combo in product(*dig)]
        return res
