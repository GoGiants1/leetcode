class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        if n < d:
            return -1
        
        @cache
        def dp(idx: int, days: int):
            if idx == n and days == 0:
                return 0
            if n - idx < days:
                return -1
            if days == 1:
                return max(jobDifficulty[idx:])
            
            max_diff = -1
            sub_prob = -1
            import math
            min_diff = math.inf
            for i in range(idx, n):
                max_diff = max(jobDifficulty[i], max_diff)
                sub_prob = dp(i + 1, days -1)
                if sub_prob == -1:
                    continue
                
                min_diff = min(min_diff, sub_prob + max_diff)
            
            return min_diff if min_diff is not math.inf else -1
        
        return dp(0, d)
                
                