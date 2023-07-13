class Solution:
    def findMin(self, nums: List[int]) -> int:

        # rotate ? 
        
        l, r = 0, len(nums) - 1
        if nums[0] < nums[-1]:
            return nums[0]

        while l < r:

            mid = (l + r) // 2
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[r]