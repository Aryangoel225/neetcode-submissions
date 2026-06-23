class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        
        counts1 = {} # value : count
        counts2 = {}
        l = 0
        r = len(s1)

        # intialise count for s1
        for ch in s1:
            counts1[ch] = 1 + counts1.get(ch, 0)
        
         # intialise count for fixed window
        for ch in s2[:len(s1)]:
            counts2[ch] = 1 + counts2.get(ch, 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if counts1 == counts2:
                return True

            # Slide the window by removing s2[l] and adding s2[r]
            counts2[s2[r]] = 1 + counts2.get(s2[r], 0)
            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                del counts2[s2[l]]
            l += 1

        # Final check after the loop for the last window
        return counts1 == counts2