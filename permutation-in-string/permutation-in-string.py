class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False

        # a to z (26 lower case)
        s_cnt = Counter(s1)
        l = 0
        seen = defaultdict(int)
        done = set()
        for r in range(m):

            c = s2[r]
            if c not in s_cnt:
                seen = defaultdict(int)
                done = set()
                l = r + 1
            else:
                if c in done:
                    while s_cnt[c] == seen[c]:
                        seen[s2[l]] -= 1
                        l += 1
                if seen[c] < s_cnt[c]:
                    seen[c] += 1
                    if seen[c] == s_cnt[c]:
                        done.add(c)
            if r - l + 1 == n:
                return True
        return False

