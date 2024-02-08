# 1208 : Get Equal substrings within budget

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = i = j = c = 0
        while j < len(s):
            c += abs(ord(s[j]) - ord(t[j]))
            while c > maxCost:
                c -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            ans = max( ans , j - i + 1 )
            j += 1
        return ans
