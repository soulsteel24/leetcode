class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        left,right = 0,len(height)-1

        while left<right:
            current_height = min(height[left],height[right])
            current_width = right-left
            current = current_height*current_width
            maxwater = max(maxwater,current)
            if height[left]>height[right]:
                right -=1
            else:
                left +=1

        return maxwater