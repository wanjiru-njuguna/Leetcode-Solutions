class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i = 0
        j = n -1
        max_area = 0
        while i < j:
            length = j - i
            if height[i] > height[j]:
                width = height[j]
                j -= 1
            else:
                width = height[i]
                i += 1

            new_max_area = length * width 
            if new_max_area > max_area:
                max_area = new_max_area
        return max_area   
            
              