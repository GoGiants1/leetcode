class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        r = k % len(nums)
        
        if len(nums) < 2 or r == 0:
            return nums
        
        nums[0:r], nums[r:] = nums[-r:], nums[0:-r]
        