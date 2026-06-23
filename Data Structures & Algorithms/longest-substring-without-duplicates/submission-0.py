class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        foundChar = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in foundChar:
                foundChar.remove(s[l])
                l += 1
            foundChar.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length