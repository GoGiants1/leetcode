class Solution:
    def isHappy(self, n: int) -> bool:
        visited_n = set()
        
        def add_powered_digits(a: int)->int:
            s = 0
            while a > 0:
                a, remain = divmod(a, 10)
                s += remain ** 2
            return s

        while n != 1:
            if n in visited_n:
                return False
            visited_n.add(n)
            n = add_powered_digits(n)

        return True