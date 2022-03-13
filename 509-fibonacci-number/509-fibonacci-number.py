from functools import lru_cache

class Solution:
    @cache
    def fib(self, n: int) -> int:
        # reuse sub problem
        memoized = []
        for i in range(n + 1):
            if i < 2:
                memoized.append(i)
                continue
            memoized.append(memoized[i - 1] + memoized[i - 2])
        return memoized[-1]

        """ Naive recursive
        def recursive_fb(n: int) -> int:
            if n < 2:
                return n
            
            return recursive_fb(n-1) + recursive_fb(n-2)
        
        return recursive_fb(n)
        """
        """
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)      
        """
        """
        a, b = 0 , 1
        
        for _ in range(n):
            a, b = b, a+b
        
        return a      
        """
