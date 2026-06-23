class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            if can_finish(k):
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1

        return res