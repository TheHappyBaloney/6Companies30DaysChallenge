# 2400. No. of ways to reach a position after exactly k steps

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 1e9 + 7

        dp = {}

        def A(currpos,k):
            if ( currpos , k ) in dp :
                return dp[( currpos , k )]

            if currpos == endPos and k == 0 :
                return 1

            if k <= 0 :
                return 0

            a,b = 0,0
            a+=A(currpos-1,k-1)
            b+=A(currpos+1,k-1)
            dp[(currpos,k)]=(a+b)%mod
            return dp[(currpos,k)]

        return int(A(startPos,k)%mod)
