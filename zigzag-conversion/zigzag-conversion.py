class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        i = 0
        dir = 1
        for j, v in enumerate(s):
            if i == numRows - 1:
                dir = -1
            elif i == 0:
                dir = 1
            rows[i].append(v)
            i += dir
        
        out = ""

        for row in rows:
            out += "".join(row)
        return out