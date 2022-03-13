class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        if nums[right] < target:
            return right + 1 # 최댓값을 넘어가는 경우 새로운 인덱스 추가
        if nums[left] >= target or right == 0: # 처음 값보다 작은 경우, 리스트 길이가 1인 경우
            return left
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] < target and nums[mid + 1] >= target:
                return mid + 1
            
            if nums[mid] >= target:
                right = mid
            elif nums[mid + 1] < target:
                left = mid + 1
