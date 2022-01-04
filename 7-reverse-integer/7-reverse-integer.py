class Solution:
    def reverse(self, x: int) -> int:
        n = str(abs(x))[::-1]
        
        if (int(n) > ((-2)**31) & int(n) > (((2)**31) - 1)):
            n = '0'
        elif x<0:
            n = '-'+n
        
        return int(n)

        