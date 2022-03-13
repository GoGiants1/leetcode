class Solution:
    def partitionString(self, s: str) -> int:
        # Sol 1. (Mine) greedy OK => Brute Force
        # f, e = 0, 1
        # subs = 1
        # while e < len(s):
        #     if s[e] in s[f:e]:
        #         f = e
        #         subs += 1
        #     e += 1
        # if e == f:
        #     subs += 1
        # return subs
        

        # Sol 2. bit manipulation

        subs = 1
        mask = 0

        for i, v in enumerate(s):
            shift = ord(v) - ord("a")
            
            if mask & (1 << shift) != 0:
                subs += 1
                mask = 0

            mask |= 1 << shift
        
        return subs
            