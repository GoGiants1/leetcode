class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp !! 
        # sub-problem이 반복된다.
        
        def dp(idx: int):
            if idx == len(nums) - 1:
                nums[idx] = (nums[idx], 0)
                return
            a, b = nums[idx + 1]
            nums[idx] = (b + nums[idx], max(a,b))
                
        
        
        for i in range(len(nums) - 1, -1, -1):
            dp(i)
        
        return max(nums[0])
            