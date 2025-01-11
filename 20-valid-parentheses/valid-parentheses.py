class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        st = []
        for braket in s:
            if braket in pair_dict:
                st.append(braket)
            else:
                if len(st) == 0 or pair_dict[st[-1]] != braket:
                    return False
                else:
                    st.pop()
        return len(st) == 0