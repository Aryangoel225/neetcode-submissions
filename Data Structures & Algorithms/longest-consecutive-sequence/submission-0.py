class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        maxLength = 0

        for n in hash_set:
            if n - 1 in hash_set:
                continue
            else:
                length = 1
                current = n
                while current + 1 in hash_set:
                    length += 1
                    current += 1
                if length > maxLength:
                    maxLength = length
        return maxLength

        