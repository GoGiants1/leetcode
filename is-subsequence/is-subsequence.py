class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Sol 1. Two ptr
        # if len(s) > len(t):
        #     return False

        # s_i = t_i = 0
        # while t_i < len(t):
        #     if s_i == len(s):
        #         return True
        #     if s[s_i] == t[t_i]:
        #         s_i += 1
            
        #     t_i += 1
        
        # return True if s_i == len(s) else False

        # Recursive and Greedy
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False
            # consume both strings or just the target string
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1

            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)