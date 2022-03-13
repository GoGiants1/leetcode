class Solution:
    def reverse(self, x: int) -> int:
        """
        if x == 0:
            return 0
        
        
        sign = x // abs(x)
        ret = str(abs(x))[::-1]
        
        if not( -2**31  <= int(ret) <= 2**31 -1):
            return 0
        
        for i,v in enumerate(ret):
            if v != "0":
                ret = ret[i:]
                break
        
        ret = '-' + ret if sign == -1 else ret
        return ret
        """
        
        sign = 1 if x > 0 else -1
        
        abs_reverse = int(str(abs(x))[::-1]) * sign
        
        return abs_reverse if -2**31 <=abs_reverse<= 2**31 -1 else 0