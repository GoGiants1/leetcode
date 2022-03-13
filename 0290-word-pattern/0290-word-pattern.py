class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Hasg map
        
        s = s.split(' ')
        
        d = {}
        
        if len(pattern) != len(s):
            return False
        
        for key, word in zip(pattern, s):
            
            if key in d:
                if d[key] != word:
                    return False
            else:
                if word in d.values():
                    return False
                d[key] = word
                
        return True