import math
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = math.sqrt(x)
        i,d = math.modf(ans)
        return int(d)

        