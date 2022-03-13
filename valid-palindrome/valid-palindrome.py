class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = set(chr(ord("a") + i) for i in range(26))

        for i in range(10):
            a.add(str(i))

        l, r = 0, len(s) - 1
        while l <= r:
            l_ch, r_ch = s[l].lower(), s[r].lower()

            if l_ch not in a:
                l += 1
                continue
            if r_ch not in a:
                r -= 1
                continue
            
            if l_ch != r_ch:
                return False
            l += 1
            r -= 1

        return True