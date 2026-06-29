class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = set()
        nums.sort()
        for i in range(len(nums)):
            target = (nums[i] * -1) 
            j, k = i + 1 , len(nums) - 1
            while j < k:
                s = nums[j] + nums[k]
                if s < target: 
                    j += 1
                elif s > target: 
                    k -= 1
                else:
                    sums.add((nums[i], nums[j], nums[k]))
                    j += 1
        return list(sums)
            

