class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums) # depth of tree
        res, sol = [], []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(sol[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:   # prune
                    continue
                sol.append(nums[i])
                backtrack(i, remaining - nums[i])   # i, not i+1 → reuse
                sol.pop()
        
        backtrack(0, target)
        return res
        