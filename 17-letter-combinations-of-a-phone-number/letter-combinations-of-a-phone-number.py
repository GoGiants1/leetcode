class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hm = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        @cache
        def dp(digit: str, st: str)->str:
            if len(digit) == 0:
                return [st] if len(st) else []
            out = []
            for ch in hm[digit[0]]:
                out.extend(dp(digit[1:], st + ch))
            return out
        
        return dp(digits, "")

