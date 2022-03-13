class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # A to Z : 26
        # 26진수네.
        from string import ascii_uppercase
        
        atoz = ""
        dic_26 = { alpha: i + 1  for i, alpha in enumerate(ascii_uppercase)}
        s = 0
        for i, a in enumerate(reversed(columnTitle)):
            s += (26 ** i) * dic_26[a]
        
        return s