class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq hashmap value -> freq
        freq = {}
        # loop through the array
        # add value and update the freq each time
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # create heap array
        # for num in key values -> heappush (freq, num)
        # if len(heap) > k pop: remove lowest value in loop as well
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        # loop thorugh for the range of k
        # append heapq.heappop[1]
        # return res
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
