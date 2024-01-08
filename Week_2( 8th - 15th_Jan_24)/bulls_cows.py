# 299. Bulls and Cows
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b , c = 0 , 0
        s = list(secret)
        g = list(guess)

        i , j = 0 , 0
        while i < len(secret):
            if s[j] == g[j]:
                s.pop(j)
                g.pop(j)
                b += 1
            else:
                j += 1
            i += 1

        temp = Counter(s)
        for l in g:
            if l in temp and temp[l] > 0 :
                c += 1
                temp[l] -= 1

        return "{}A{}B".format( b , c )
