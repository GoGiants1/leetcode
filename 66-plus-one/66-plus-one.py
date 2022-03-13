class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        else:
            c = 1
            for i in range(len(digits) - 1, -1, -1):
                
                s = digits[i] + c
                # print(i, digits[i], c)
                if s == 10:
                    c = 1
                    digits[i] = 0
                else:
                    c = 0
                    digits[i] = s
            
            if c == 1:
                digits.insert(0, 1)
            return digits