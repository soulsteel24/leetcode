class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mini = float('inf')

        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] <= mini:
                mini = nums[mid]

            if nums[mid]>nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        
        return mini