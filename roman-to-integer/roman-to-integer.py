class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        # out = 0
        # st = []
        # n = len(s)
        # i = 0
        # while i < n:
        #     if i + 1 < n:
        #         if s[i:i+2] in sym:
        #             out += sym[s[i:i+2]]
        #             i += 2
        #         else:
        #             out += sym[s[i]]
        #             i += 1
        #     else:
        #         out += sym[s[i]]
        #         i += 1
    
        # return out
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total