class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # n = len(nums)
            
        # l = r = s = 0
        # sz = math.inf
        # while r < n + 1 and l <= r:
        #     if s >= target:
        #         sz = min(sz, r-l)
        #         s -= nums[l]
        #         l += 1
        #     else:
        #         if r < n:
        #             s += nums[r]
        #         r += 1
        
        # return sz if sz != math.inf else 0
        
        l = 0
        sum_of_curr_wdw = 0
        sz = math.inf
        n = len(nums)
        for r in range(n):
            sum_of_curr_wdw += nums[r]
            while sum_of_curr_wdw >= target:
                sz = min(sz, r-l+1)
                sum_of_curr_wdw -= nums[l]
                l += 1
            
        return sz if sz != math.inf else 0
            