class Solution:
    def mySqrt(self, x: int) -> int:
        """
        binary search 이용?
        1 1
        2 4
        3 9
        4 16
        5 25
        6 36
        7 49
        8 64
        9 81
        10 100
        11 121
        """
        """Brute Force
        if x == 0:
            return 0
        sq = 0
        for a in range(x+1):
            s = a * a
            if s <= x:
                sq = a
            else:
                break
        
        
        return sq
        """
        if x==1: return 1 #deal with exception
        l, r = 0, x
        while l <= r:
            mid = (r+l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid
       