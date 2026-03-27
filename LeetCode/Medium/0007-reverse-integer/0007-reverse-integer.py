class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0
        while num > 0:
            res = (res * 10) + (num % 10)
            num //= 10
        
        if res < -2**31 or res > (2**31)-1:
            return 0
        
        return res if x > 0 else -res
