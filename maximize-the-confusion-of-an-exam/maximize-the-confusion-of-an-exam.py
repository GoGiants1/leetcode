class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        from collections import deque
        n = len(answerKey)
        t_cnt = f_cnt = 0
        T = "T"
        F = "F"
        l = 0
        ans = 0

        # increase right answerKey count
        # if Both of T, F counts are smaller or equal to k: continue
        # else: iterate until cond 1 is satisfied

        # store max consecutive length
        for r in range(n):
            if answerKey[r] == T:
                t_cnt += 1
            else:
                f_cnt += 1
            
            if t_cnt > k and f_cnt > k:
                while not (t_cnt <= k or f_cnt <= k):
                    if answerKey[l] == T:
                        t_cnt -= 1
                    else:
                        f_cnt -= 1
                    l += 1
            # print(f"l: {l}, r: {r}, (t_cnt, f_cnt): ({t_cnt}, {f_cnt})")
            ans = max(ans, r - l + 1)
        return ans

            

