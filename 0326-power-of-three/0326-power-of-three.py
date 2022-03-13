class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        r = 0
        while n > 1:
            n, r = divmod(n, 3)
            if r != 0:
                return False
            
        if r != 0 :
            return False
        return True