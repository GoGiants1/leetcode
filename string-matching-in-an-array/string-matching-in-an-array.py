class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        words.sort(key=lambda x: -len(x))
        out = []
        visited = set()
        for i, w in enumerate(words):
            for j in range(i+1, len(words)):
                if j not in visited and words[j] in w:
                    out.append(words[j])
                    visited.add(j)
        return out