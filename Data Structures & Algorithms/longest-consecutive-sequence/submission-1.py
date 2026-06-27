class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert array to set
        nums = set(nums)
        count = 0
        max = 0
        # loop through the set
        for num in nums:
            if (num - 1) in nums:
                continue 
            else:
                count += 1
                while (num + 1) in nums:
                    count += 1
                    num += 1
                if count > max:
                    max = count
            count = 0
        return max
            

                

        # count = 
        # max =
        # for each num if a num - 1 doesn't exist 
        # add to count then save current num
        # check if another num + 1 exist in set in while loop while adding to cout
        # until max then add to max and move on
        # return max at end