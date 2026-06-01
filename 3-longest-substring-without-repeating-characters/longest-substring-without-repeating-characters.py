class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        left = 0
        count = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left +=1
            
            charset.add(s[right])
            current = right - left + 1
            count = max(count, current)
        return count