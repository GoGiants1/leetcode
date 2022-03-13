class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """ 
            Brute Force O(m*n)
        if not needle:
            return 0
        len_h = len(haystack)
        ret = -1
        for i, v in enumerate(haystack):
            if v != needle[0]:
                continue
            is_needle = True
            for j, w in enumerate(needle):
                if i + j >= len_h:
                    is_needle = False
                    break
                if haystack[i + j] != w:
                    is_needle = False
            if is_needle:
                ret = i
                break
        return ret
        """

        """
            TODO: Implement KMP Algorithm
        """
        
        """
            Implement Rolling hash
        """
        
        if not needle:
            return 0
        len_h = len(haystack)
        len_n = len(needle)
        
        if len_h == 0 or len_h < len(needle):
            return -1
        
        target_hash = hash(needle)
        
        for i in range(len_h):
            h_hash = hash(haystack[i: i + len_n])
            if target_hash == h_hash:
                if needle == haystack[i:i+len_n]:
                    return i

        return -1
        
        
        
        