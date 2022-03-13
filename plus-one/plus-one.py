class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            carry, res = divmod(digits[i] + carry, 10)
            digits[i] = res
            if carry == 0:
                break
        if carry:
            digits.insert(0, 1)
        return digits