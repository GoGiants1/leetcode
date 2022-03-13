class Solution:             
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        w_set = set(wordDict)

        @cache
        def dp(curr: int):
            if curr == len(s):
                return True
            elif curr > len(s):
                return False
            out = False
            for w in w_set:
                if s[curr : curr + len(w)] == w:
                    out = dp(curr + len(w))
                    if out == True:
                        return True
        
        return dp(0)