class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            
        # log n => bin search
        def binSearch(start: int, end: int)-> int:
            
            mid = (start + end) // 2
            
            if nums[start] <= target <= nums[end]:           
                if nums[mid] == target:
                    return mid            
                elif nums[mid] > target:
                    mid = binSearch(start, mid -1)
                else:
                    mid = binSearch(mid + 1, end)
            elif target < nums[start]:
                return start
            else:
                return end + 1
            return mid
        return binSearch(0, len(nums) -1)