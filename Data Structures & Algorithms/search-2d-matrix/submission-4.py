class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        # Binary search to find the correct row
        while top <= bottom:
            mid = (top + bottom) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                bottom = mid - 1
        else:
            return False  # target not in any row range

        # Binary search inside the row
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1

        return False