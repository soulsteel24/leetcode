class Solution:
    def trap(self, height: List[int]) -> int:
        l,l_max = 0,0
        water = 0
        r,r_max = len(height)-1,0
        while l<=r:
            l_max=max(height[l],l_max)
            r_max=max(height[r],r_max)
            
            if height[l]<height[r]:
                water += l_max - height[l]
                l += 1
            else:
                water += r_max - height[r]
                r -=1
        return water
                 