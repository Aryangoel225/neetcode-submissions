class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        foundChar = set()
        maxLength = 0

        for r in range(len(s)):
            while s[r] in foundChar:
                foundChar.remove(s[l])
                l += 1
            foundChar.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            
        return maxLength
        
            

        