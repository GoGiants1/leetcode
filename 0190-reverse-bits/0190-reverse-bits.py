class Solution:
    def reverseBits(self, n: int) -> int:
        b = []
        while n > 0:
            b.append(str(n & 1))
            n = n >> 1
        s = 0
        for i, v in enumerate(reversed(b)):
            s += 2 ** i * int(v)
        
        s = s * (2 ** (32 -len(b)))
            
        return s