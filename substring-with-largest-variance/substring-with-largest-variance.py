class Solution:
    def largestVariance(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for a, b in itertools.product(set(s), set(s)):
            if a == b: continue
            cnt_a, cnt_b, remains_b = 0, 0, cnt[b]
            for ch in s:
                if ch == a: cnt_a += 1
                elif ch == b: 
                    cnt_b += 1
                    remains_b -= 1
                
                if cnt_b: ans = max(ans, cnt_a - cnt_b)
                if cnt_a < cnt_b and remains_b > 0:
                    cnt_a, cnt_b = 0, 0
        
        return ans