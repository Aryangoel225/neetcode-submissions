from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int) #hashmap of char to count
        l = 0
        res = 0

        for r in range(len(s)):
            counter[s[r]] += 1

            # if len(substr) - most frequent char> k, move l and remove l value form counter
            if ((r - l + 1) - max(counter.values())) > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        return res
