class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # set k and nums as a val and min-heap
        self.k  = k
        heapq.heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
