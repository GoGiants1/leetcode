class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        
        for a, b in  zip(sorted(s_cnt.most_common()), sorted(t_cnt.most_common())):
            if a[0] == b[0] and a[1] ==b[1]:
                continue
            else:
                return False
        return True