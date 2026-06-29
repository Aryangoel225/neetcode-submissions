class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea, area = 0, 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > maxArea:
                maxArea = area
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return maxArea
            
            

        