class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        max_length = 0

        for n in num:
            if (n-1) not in num:
                current = n
                current_streak = 1

                while (current + 1) in num:
                    current += 1
                    current_streak += 1
                max_length = max(max_length, current_streak)
        
        return max_length