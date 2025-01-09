class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sub_idx = 0
        t_idx = 0
        m = len(s)
        n = len(t)
        while sub_idx < m and t_idx < n:
            if s[sub_idx] == t[t_idx]:
                sub_idx += 1
                t_idx += 1
            else:
                t_idx +=1
        
        return sub_idx == m