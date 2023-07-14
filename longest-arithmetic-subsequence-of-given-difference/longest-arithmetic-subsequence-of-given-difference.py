class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        last_cnt = {}

        for i, v in enumerate(arr):
            if v - difference in last_cnt:
                last_cnt[v] = last_cnt[v - difference] + 1
            else:
                last_cnt[v] = 1
        
        return max(last_cnt.values())