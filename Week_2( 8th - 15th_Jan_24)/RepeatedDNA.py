class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 10
        substrings = [s[i:i + l] for i in range(0, len(s) - l + 1) if len(s[i:i + l]) == l]
        
        rep = set()
        n = set()

        for j in substrings:
            if j in n:
                rep.add(j)
            else:
                n.add(j)
        return list(rep)
