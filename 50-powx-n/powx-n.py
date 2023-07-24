class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            x, n = 1 / x, -n
        
        @cache
        def fn(m: int)->float:
            if m == 1:
                return x
            
            if m % 2 == 0:
                return fn(m // 2) ** 2
            else:
                return fn(m - 1) * x

        return fn(n)