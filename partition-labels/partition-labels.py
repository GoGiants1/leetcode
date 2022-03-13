class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {c: i for i, c in enumerate(s)}

        left = end = 0
        out = []
        for i, v in enumerate(s):
            end = max(end, last_idx[v])
            if i == end:
                out.append(end-left+1)
                left = end = i + 1
        return out