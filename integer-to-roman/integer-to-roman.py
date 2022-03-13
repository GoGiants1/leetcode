class Solution:
    def intToRoman(self, num: int) -> str:

        val_sym = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        val_list = sorted(list(val_sym.keys()), reverse=True)
        i = 0
        out = []
        while num > 0:
            if val_list[i] <= num:
                num -= val_list[i]
                out.append(val_sym[val_list[i]])
            else:
                if i < len(val_list):
                    i += 1
                else:
                    break
        
        return "".join(out)