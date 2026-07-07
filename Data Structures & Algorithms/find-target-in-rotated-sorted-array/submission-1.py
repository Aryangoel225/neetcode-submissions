class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[lo]: # if true sorted bit, false otherwise
                if nums[lo] <= target < nums[mid]: # if target is in, move hi
                    hi = mid - 1
                else: # else out in the other half move lo
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]: # if target is in, move lo
                    lo = mid + 1
                else: # else out in the other half move hi
                    hi = mid - 1
        return idx

            # find the drop by  mid > hi 
            # but how to know if target is in the min or hi portion 
            # mid <= hi

