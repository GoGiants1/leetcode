class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        # l = r = 0
        # dup = set()
        # size = 0
        # mx_sz = 0
        # for r in range(n):
        #     while s[r] in dup:
        #         dup.discard(s[l])
        #         l += 1
        #     dup.add(s[r])
        #     size = r - l + 1
        #     mx_sz = max(mx_sz, size)
        
        # return mx_sz 
        used = {}
        mx_len = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                mx_len = max(mx_len, i - start + 1)
            
            used[c] = i
            
        return mx_len