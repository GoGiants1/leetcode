class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
#         cols = list(zip(*strs))

#         out = 0
        
#         for i, c in enumerate(cols):
#             prev = None
#             for j, w in enumerate(c):
#                 if prev is None:
#                     prev = ord(w)
#                 if prev - ord(w) > 0:
#                     out += 1
#                     break
#                 else:
#                     prev = ord(w)

#         return out

        out = 0
        
        for i in range(len(strs[0])):
            prev = None
            for j in range(len(strs)):
                if prev is None:
                    prev = ord(strs[j][i])
                    continue
                if prev - ord(strs[j][i])> 0:
                    out += 1
                    break
                else:
                    prev = ord(strs[j][i])

        return out