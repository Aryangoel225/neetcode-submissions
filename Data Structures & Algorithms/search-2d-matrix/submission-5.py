class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1 # number of rows
        while l <= r:
            idx = l + ((r - l) // 2)
            mid = matrix[idx][0]
            if mid < target:
                l = idx + 1
            elif mid > target:
                r = idx - 1
            else:
                return True # if the answer is in first col
        
        row = r
        if r < 0 or r > len(matrix) - 1:
            return False
        
        # after first while loop breaks, the idx will equal row that might hold it
        l, r = 0, len(matrix[0]) - 1 # number of cola
        while l <= r:
            idx = l + ((r - l) // 2)
            mid = matrix[row][idx]
            if mid < target:
                l = idx + 1
            elif mid > target:
                r = idx - 1
            else:
                return True
        
        return False
        
        