class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1) ,len(word2)

        @cache
        def dp(i:int, j:int):
            if i == m and j == n:
                return 0
            elif i >= m:
                return n - j
            elif j >= n:
                return (m - i)
            elif word1[i] == word2[j]:
                return dp(i+1, j+1)
            else:
                out = []
                # delete
                out.append(dp(i + 1, j) + 1)
                # insert
                out.append(dp(i, j + 1) + 1)
                # replace
                out.append(dp(i + 1, j + 1) + 1)
                return min(out)
        
        return dp(0,0)