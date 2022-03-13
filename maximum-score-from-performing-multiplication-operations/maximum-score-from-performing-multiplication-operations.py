class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # State variable  multiplier[i], left or right index in nums
        # Base Case 
        # n = len(nums)
        # m = len(multipliers)
        
        # @cache
        # def dp(l:int, r: int, mul_idx: int):
        #     if mul_idx >= m:
        #         return 0
            
        #     left = dp(l+1, r, mul_idx + 1) + nums[l] * multipliers[mul_idx]
        #     right = dp(l, r-1, mul_idx + 1) + nums[r] * multipliers[mul_idx]

        #     return max(left, right)
        # return dp(0, n-1, 0)

        # Bottom-Up

        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - 1 - (i - left)
                dp[i][left] = max(mult * nums[left] + dp[i + 1][left + 1], 
                                  mult * nums[right] + dp[i + 1][left])        
        return dp[0][0]
