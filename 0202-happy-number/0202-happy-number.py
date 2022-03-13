class Solution:
    def isHappy(self, n: int) -> bool:
        # 각 자리 숫자의 제곱의 합을 n으로 교체
        # n이 1이 될때까지 반복.
        # 1이 되면 happy
        
        s = set()
        
        
        
        while n != 1:
            if n in s:
                return False
            s.add(n)
            acc = 0
            while n > 0:
                n, remainder = n // 10, n % 10
                
                acc += remainder ** 2
            n = acc
        
        return True