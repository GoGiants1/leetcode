class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # find pivot idx
        # l, r = 0, len(nums) - 1
        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return 0
        #     else:
        #         return -1
        # if nums[0] < nums[-1]:
        #     idx = bisect.bisect_left(nums, target)
        #     if idx <= r and nums[idx] == target:
        #         return idx
        #     else:
        #         return -1
        # # find pivot idx

        # while l < r:
        #     mid = (l+r) // 2
            
        #     if nums[mid] > nums[r]:
        #         # find target
        #         l = mid + 1
        #     else:
        #         r = mid

        # pivot = r - 1

        # if nums[0] <= target <= nums[pivot]:
        #     l, r = 0, pivot
        # else:
        #     l, r = pivot + 1, len(nums) - 1

        # while l < r:
        #     mid = (l+r) // 2
            
        #     if nums[mid] < target:
        #         # find target
        #         l = mid + 1
        #     else:
        #         r = mid

        # if nums[r] == target:
        #     return r
    
        # return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid]< target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1