class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l,total_sum = 0, sum(nums)
        idx = 0
        min_avg = math.inf
        for i in range(len(nums)):
            l += nums[i]
            if i == len(nums) -1:
                new_avg = l // (i+1)
            else:
                new_avg = abs(l // (i+ 1) - ((total_sum -l) // (len(nums) - i - 1)))
            if min_avg > new_avg:
                idx, min_avg = i, new_avg
        
        return idx
            
        