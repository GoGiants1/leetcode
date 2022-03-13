class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # s = a + b
        # len(vowels(a)) == len(vowels(b)) is True
        # else False
        
        vowels = ["a", "e", "i", "o", "u"]
        
        s = s.lower()
        
        a, b = s[ : len(s) // 2], s[len(s)//2 : ]
        a_vowel_cnt = 0
        b_vowel_cnt = 0
        
        for i, v in enumerate(vowels):
            a_vowel_cnt += a.count(v)
            b_vowel_cnt += b.count(v)
            
        if a_vowel_cnt == b_vowel_cnt:
            return True
        else:
            return False