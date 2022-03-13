class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 실제 프로덕트에선 정규표현식 이용하면 될 듯
        if not s: return True
        pos = 0
        for ch in t:
            if ch == s[pos]:
                pos += 1
                if pos == len(s):
                    return True
        return False
        