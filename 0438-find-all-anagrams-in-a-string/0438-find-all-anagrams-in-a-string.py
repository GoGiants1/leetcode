class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return array
        # start indices of p's anagrams in s. order X
        # Sliding window
        d = {}
        k = len(p)
        out = []
        
        
        from collections import Counter
        p_cnt = Counter(p)
        s_cnt = Counter(s[:k])
        
        
        def check_anagram(c1: Counter,c2:Counter):
            if c1 == c2:
                return True
            
            return False
        
        
        for i in range(len(s)):
            if check_anagram(s_cnt, p_cnt):
                out.append(i)
            s_cnt[s[i]] -= 1
            if i + k < len(s):
                s_cnt[s[i+ k]] += 1

        return out
        