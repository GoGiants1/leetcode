class Solution:
    def reverseWords(self, s: str) -> str:
        st = []
        for i, v in enumerate(s.split(" ")):
            if v != "":
                st.append(v)
            
        
        return " ".join(st[::-1])