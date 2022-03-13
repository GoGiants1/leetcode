class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        #two pointer

        a = len(word1)
        b = len(word2)

        new_word = []

        id1 = id2 = 0
        while id1 < a and id2 < b:
            
            new_word.append(word1[id1])
            new_word.append(word2[id2])

            id1 += 1
            id2 += 1
        out = "".join(new_word)
        if id1 < a:
            return out + word1[id1:]
        elif id2 < b:
            return out + word2[id2:]
        else:
            return out