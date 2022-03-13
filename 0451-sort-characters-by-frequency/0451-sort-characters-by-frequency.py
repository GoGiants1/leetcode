class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        cnt = Counter(s)
        
        chars = cnt.most_common()
        l = []
        for a, i in chars:
            l.append(a*i)
        
        return ''.join(l)