#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        if n == 1:
            return heights[0]
        #we need to move <-- left and right --> untill we find smaller bar
        # considering current bar as smallest bar possible
        for i in range(n):
            current = heights[i]

            # moving left till we get smaller height bar
            left = i
            while left>=0 and heights[left]>=current:
                left -= 1 #moving index left

            # moving right index to right untill we get end or smaller height bar 
            right = i
            while right<n and heights[right]>=current:
                right +=1
            # calculating width and area:
            width = right - left - 1
            area = width * current
            max_area = max(area,max_area)
        return max_area
             
# @lc code=end

