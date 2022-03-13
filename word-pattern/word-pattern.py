class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(' ')
        hm = {}
        used_wd = set()
        if len(pattern) != len(words):
            return False
        for i, v in enumerate(pattern):
            if v in hm:
                if hm[v] != words[i]:
                    return False
            else:
                if words[i] in used_wd:
                    return False
                hm[v] = words[i]
                used_wd.add(words[i])
        return True