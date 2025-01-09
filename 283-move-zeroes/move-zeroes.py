class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        n = len(nums)
        while l < n and r < n:
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                continue
            if nums[l] != 0:
                l += 1
            r += 1

            