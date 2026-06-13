class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in hash_map:
                return [hash_map[remaining],i]
            hash_map[nums[i]] = i