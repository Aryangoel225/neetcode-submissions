class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res, sol = [], []
        
        # backtracking
        def backtrack(start, remaining):
            # base case
            if remaining == 0:
                res.append(sol[:])
                return
            
            # for loop through all options
            for i in range(start, len(candidates)):
                # skipp the neighbor node
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # if num value is greater than remainder
                if candidates[i] > remaining:
                    continue 
                sol.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                sol.pop()



        
        backtrack(0, target)
        return res