class Solution:
    def climbStairs(self, n: int) -> int:
        # a * 1 + b * 2 = n

        
        ways = 0
        
        def count_ways(cnt1:int, cnt2:int) -> int:
            if cnt1 == 0 or cnt2 == 0:
                return 1
            
            return math.factorial(cnt1 + cnt2) // (math.factorial(cnt1) * (math.factorial(cnt2)))
        
        for i in range(0, n // 2 + 1):
            ways += count_ways(i, n - 2 * i)
            
        return ways