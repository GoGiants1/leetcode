class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        upper = string.ascii_uppercase
        
        lower = string.ascii_lowercase
        
        # True True True
        
        # True False False
        
        # False False False
        
        out = []
        first = True if word[0] in upper else False
        
        for i, v in enumerate(word[1:]):
            out.append(v in upper)
        
        
        after_first_is_capital = all(out)
        after_first_is_lower = not any(out)
        
        
        return (first and after_first_is_lower) or (not first and after_first_is_lower) or (first and after_first_is_capital)