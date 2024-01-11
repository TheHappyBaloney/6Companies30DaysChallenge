#683. Shopping offers

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}

        def sp(offer, needs):
            for i in range(len(needs)):
                if needs[i] < offer[i]:
                    return False
            return True

        def apply(offer, needs):
            new_needs = list(needs)
            for i in range(len(new_needs)):
                new_needs[i] -= offer[i]
            return new_needs

        def cost(needs):
            c = 0
            for i in range(len(needs)):
                c += needs[i] * price[i]
            return c

        def min_price(needs):
            if sum(needs) == 0:
                return 0

            if tuple(needs) in memo:
                return memo[tuple(needs)]

            total = cost(needs)
            final = total

            for offer in special:
                if sp(offer, needs):
                    new_needs = apply(offer, needs)
                    final = min(final, offer[-1] + min_price(new_needs))

            memo[tuple(needs)] = final
            return final

        return min_price(needs)
