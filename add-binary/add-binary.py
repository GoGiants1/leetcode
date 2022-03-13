class Solution:
    def addBinary(self, a: str, b: str) -> str:
            
        if len(a) < len(b):
            a ,b = b, a
        l = len(a) - 1
        r = len(b) - 1
        out = []
        carry = 0
        while l >= 0 and r >= 0:
            v, w = int(a[l]), int(b[r])
            carry, res = divmod(v + w + carry, 2)
            out.append(str(res))
            l -= 1
            r -= 1

        while l >= 0:
            carry, res = divmod(int(a[l]) + carry, 2)
            out.append(str(int(res)))
            l -= 1
        if carry:
            out.append("1")
        return ''.join(out[::-1])
