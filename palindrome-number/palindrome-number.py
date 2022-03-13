class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        # find digit count

        m = math.floor(math.log10(x))
        a = b = 0
        for i in range(m // 2 + 1):
                a = x // pow(10, i) % 10
                b = x // pow(10, m - i) % 10
                if a != b :
                    return False
        return True

        
