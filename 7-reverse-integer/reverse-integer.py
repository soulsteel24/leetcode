class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 **31 -1

        sign = -1 if x<0 else 1
        x = abs(x)
        
        result = 0
        while x != 0:
                digit = x%10
                x = x//10
                if result > (MAX-digit)//10:
                    return 0
                result = result * 10 + digit
        return result * sign