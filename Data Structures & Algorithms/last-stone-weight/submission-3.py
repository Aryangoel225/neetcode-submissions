class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a heap of the stone list
        for i, stone in enumerate(stones):
            stones[i] = -1 * stone
        # create a max heap
        heapq.heapify(stones)

        
        # while lenght of heap > 1
        while len(stones) > 1:
            # pop two value from heap
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            # math
            if x == y:
                continue
            else:
                y = y - x
            # add to the heap
            heapq.heappush(stones, (y * -1))

        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0
    
        
        