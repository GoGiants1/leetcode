class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        
        for i, n in enumerate(nums):
            
            nums[i] = acc + nums[i]
            
            acc = nums[i]
        
        return nums