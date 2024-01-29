#2572. Count the no. of square free subsets

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cn = Counter(nums)
        mod  = 10**9 + 7
        n = len(primes)
        f = [0] * (1 << n)
        f[0] = pow(2, cn[1], mod)
        for x in range(2, 31):
            is_square_free = True
            for p in primes:
                if x % (p * p) == 0:  
                    is_square_free = False
                    break
            if not is_square_free:
                continue
            mask = 0
            
            for i, p in enumerate(primes):
                if x % p == 0:
                    mask |= 1 << i
            for state in range((1 << n) - 1, 0, -1):
                if state & mask == mask:
                    f[state] = (f[state] + cn[x] * f[state ^ mask]) % mod
        total_sum = sum(v for v in f)
        return (total_sum - 1) % mod if total_sum != 0 else mod - 1
