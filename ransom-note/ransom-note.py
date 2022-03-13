class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        cnt_m = Counter(magazine)
        cnt_r = defaultdict(int)
        for i, v in enumerate(ransomNote):
            cnt_r[v] += 1
            if cnt_r[v] > cnt_m[v]:
                return False
        
        return True