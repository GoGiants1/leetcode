class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = -1
        from collections import Counter
        
        cnt = Counter(s)
        for i, v in enumerate(s):
            if cnt[v] == 1:
                idx = i
                break
        
        return idx