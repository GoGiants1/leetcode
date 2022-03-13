class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        chars = list(zip(*strs))


        out = []

        for i, v in enumerate(chars):
            if len(set(v)) == 1:
                out.append(v[0])
            else:
                break
        return "".join(out)