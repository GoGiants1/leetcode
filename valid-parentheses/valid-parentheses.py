class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_s = set(["(","[", "{"])
        close_s = set([")", "]","}"])
        pair = {"(": ")", "{": "}", "[": "]"}
        for i, v in enumerate(s):
            if v in open_s:
                st.append(v)
            else:
                if not st:
                    return False
                w = st.pop()
                if pair.get(w, "") != v:
                    return False
        
        return True if len(st) == 0 else False
