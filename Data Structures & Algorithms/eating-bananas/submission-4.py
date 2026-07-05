from math import ceil

class Solution:
    def totalHours(self, k: int, piles: List[int]) -> int:
        total = 0
        for pile in piles:
            total += ceil(pile / k)
        return total 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (hi + lo) // 2
            if self.totalHours(k, piles) <= h:
                hi = k
            else:
                lo = k + 1
        
        return lo

    


        