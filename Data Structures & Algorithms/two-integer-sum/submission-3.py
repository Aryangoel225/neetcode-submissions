class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value: index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap.get(diff), i]
            else:
                hashmap[nums[i]] = i
        return [0,0]