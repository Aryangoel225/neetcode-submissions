class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a minheap out of nums
        # keep it under len k by popping small values
        # take the k popped value and return it
        minheap = []
        for num in nums:
            heapq.heappush(minheap, (num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        return heapq.heappop(minheap)
            
        


