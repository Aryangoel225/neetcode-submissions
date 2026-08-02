from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        s1_count = Counter(s1)
        window_count = Counter()
        l = 0

        for r in range(len(s2)):
            # add new elements to window
            window_count[s2[r]] += 1

            # if the window exceeds size k, remove left most element
            if r - l + 1 > k:
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1

            if r - l + 1 == k and window_count == s1_count:
                return True

        return False
        


        