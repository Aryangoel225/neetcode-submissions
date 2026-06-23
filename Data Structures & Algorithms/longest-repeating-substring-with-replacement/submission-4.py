class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        maxf = 0

        for i, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)
            maxf = max(maxf, count[char])

            while (i - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, i - l + 1)

        return res