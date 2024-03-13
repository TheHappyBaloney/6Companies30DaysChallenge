# 1994. The Number of Good Subsets

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        cands = {}
        for x in range(1, 31):
            orig = x
            mask = 0
            for p in primes:
                if x % p: continue
                if p > x: break
                x //= p
                mask ^= (1 << p)
            if x == 1:
                cands[orig] = mask


        cnt = {k: v for k, v in Counter(nums).items() if k in cands}
        cnt_key = list(filter(lambda x: x> 1, sorted(cnt)))
        n = len(cnt_key)
        M = 10**9 + 7
        
        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return mask > 0
            ans = dp(i+1, mask)
            if mask & cands[cnt_key[i]] == 0:
                ans += cnt[cnt_key[i]] * dp(i+1, mask ^ cands[cnt_key[i]])
            return ans % M
        
        return (dp(0, 0) * pow(2, cnt.get(1, 0))) % M
