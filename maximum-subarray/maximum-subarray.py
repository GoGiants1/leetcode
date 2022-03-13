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
        
        currSum = 0
        maxSum = nums[0]

        for n in nums:
            if n > currSum and currSum < 0:
                currSum = n
            else:
                currSum += n
            if currSum > maxSum:
                maxSum = currSum
        return maxSum