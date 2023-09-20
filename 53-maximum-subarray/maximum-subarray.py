class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # find the subarray
        # Sol 1. DP
        # mx = -math.inf
        # n = len(nums)
        # # dp[i] = (dp[i-1] + nums[i], nums[i])
        # committed = ing = nums[0]
        # for i in range(1, n):
        #     committed, ing = max(committed, ing), max(nums[i], ing+nums[i]) 
        
        # return max(committed, ing)
        
        curr_sum = 0
        max_sum= nums[0]

        for n in nums:
            if n > curr_sum and curr_sum < 0:
                curr_sum = n
            else:
                curr_sum += n
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum