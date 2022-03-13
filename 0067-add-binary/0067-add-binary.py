class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        
        while y:
            x, y = x ^ y, (x & y) << 1
        
        return bin(x)[2:]
        
# My First Solution
#         if a == '0':
#             return b
#         if b == '0':
#             return a
        
#         max_len = max(len(a), len(b))
#         if len(b) == max_len:
#             a, b = b, a
#         a = list(a)
#         b = list(b)
#         carry = 0
#         dq = deque()
#         for i in range(max_len):
#             a_digit = int(a.pop())
#             b_digit = 0
            
#             if len(b) > 0:
#                 b_digit = int(b.pop())
            
#             carry, s = divmod(a_digit + b_digit + carry, 2)
            
#             dq.appendleft(str(s))
#         if carry == 1:
#             dq.appendleft(str(carry))
#         return "".join(list(dq))

        
            
            
        