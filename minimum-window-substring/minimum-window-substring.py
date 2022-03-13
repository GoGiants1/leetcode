class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        cnt_t = Counter(t)
        l = 0
        seen = defaultdict(int)
        ok = set()
        min_wdw = ""
        for r in range(len(s)):
            if s[r] in cnt_t:
                seen[s[r]] += 1
            else:
                continue
            
            if seen[s[r]] == cnt_t[s[r]]:
                ok.add(s[r])
            while len(ok) == len(cnt_t):
                if len(min_wdw) == 0 or len(min_wdw) > r - l + 1:
                    min_wdw = s[l:r+1]
                if s[l] in seen:
                    seen[s[l]] -= 1
                    if seen[s[l]] < cnt_t[s[l]]:
                        ok.discard(s[l])
                l += 1
            
        return min_wdw



