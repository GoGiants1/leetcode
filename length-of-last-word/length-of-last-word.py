class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # l = s.split(" ")

        # for i in range(len(l)-1, -1, -1):
        #     if l[i] != "":
        #         return len(l[i])
        #     else:
        #         continue
        n = len(s)
        out = -1
        for i in range(n-1, -1, -1):
            if out == -1: 
                if s[i] == " ":
                    continue
                else:
                    out = 1
                    continue
            else:
                if s[i] == " ":
                    return out
                else:
                    out += 1
        
        return out