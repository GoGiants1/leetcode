class Solution:
    def isPalindrome(self, s: str) -> bool:
        from string import ascii_letters, digits
        l, r = 0, len(s) - 1
        alphabet = set(ascii_letters + digits)
        while l < r:
            if s[l] not in alphabet:
                l += 1
                continue
            elif s[r] not in alphabet:
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
            
            