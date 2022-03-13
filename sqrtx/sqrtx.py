class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 0, x // 2 + 1


        while l < r :
            mid = (l + r) // 2
            if mid ** 2 < x:
                l = mid + 1
            elif mid ** 2 == x:
                return mid
            else:
                r = mid
        
        return l - 1
            
        
