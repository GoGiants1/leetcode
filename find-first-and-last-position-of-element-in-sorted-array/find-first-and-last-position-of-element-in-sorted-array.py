class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = end = -1

        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if l < len(nums) and nums[l] == target:
            start = l
        else:
            return [start, end]
        r = len(nums)
        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        
        if l - 1 < len(nums) and nums[l - 1] == target:
            end = l - 1
        return [start, end]