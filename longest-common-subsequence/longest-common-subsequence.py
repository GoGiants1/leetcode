class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # status variable: index from text 1 and index from text 2
        # recurrence relation 
        # base case => text len is 0
        len1, len2 = len(text1), len(text2)
        @cache
        def dp(idx1, idx2):
            if idx1 == len1 or idx2 == len2:
                return ""
            
            if text1[idx1] == text2[idx2]:
                return text1[idx1] + dp(idx1+1, idx2+1)
            else:
                left, right = dp(idx1+1, idx2), dp(idx1, idx2+1)
                return left if len(left) > len(right) else right
        
        return len(dp(0,0))