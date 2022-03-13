class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(1, numRows + 1):
            base = [1 for j in range(i)]
            if i > 2:
                for j in range(1, len(base) // 2 + 1):
                    base[j] = base[-j-1] = out[i- 2][j - 1] + out[i- 2][j]
            out.append(base)
        return out
#     0
#    0 1
#   0 1 2
#  0 1 2 3
# 0 1 2 3 4