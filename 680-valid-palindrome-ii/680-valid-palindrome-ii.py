class Solution:
    def validPalindrome(self, s: str) -> bool:
        """Sol 1
        def recursive_check(start, end, is_deleted = False):
            if start > end:
                return True
            ret = None
            remove_left = None
            remove_right = None
            
            if s[start] == s[end]:
                ret = recursive_check(start + 1, end - 1, is_deleted)
            else:
                if not is_deleted:
                    is_deleted = True
                    remove_left = recursive_check(start + 1, end, is_deleted)
                    remove_right = recursive_check(start, end - 1, is_deleted)
                else:
                    return False
            if ret is None:
                return remove_left or remove_right
            else:
                return ret
            
        
        return recursive_check(0, len(s) -1, False)
        """
        """
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left+1:right+1]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
            
        return True