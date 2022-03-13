class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        for t_ch in t_cnt:
            if t_ch not in s_cnt:
                return False
            elif t_cnt[t_ch] != s_cnt[t_ch]:
                return False
    
        return True