class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # track the num and freq
        for n in nums:
            count[n] = 1 + count.get(n, 0) # fill in the map num : freq

        freq = [[] for i in range(len(nums) + 1)] # bucket

        for n , c in count.items(): # fill the bucket with count as index and num as value
            freq[c].append(n)
        
        res = [] # list to return
        for i in range((len(freq) -1 ), 0, -1): # iterate backwards
            for n in freq[i]: # for the 
                res.append(n)
                if len(res) == k:
                    return res        


