class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        used_t = set()
        for i in range(len(s)):
            if s[i] in s_to_t:
                if s_to_t[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in used_t:
                    return False
                else:
                    s_to_t[s[i]] = t[i]
                    used_t.add(t[i])
        return True