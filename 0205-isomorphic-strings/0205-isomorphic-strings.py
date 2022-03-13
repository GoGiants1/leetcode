class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 알파벳 to 알파벳 으로 변경
        # counter 이용하면 쉬울 듯.
        
        dic = {}
        
        for i in range(len(s)):
            if s[i] in dic:
                if t[i] != dic[s[i]]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
                dic[s[i]] = t[i]
        return True
    