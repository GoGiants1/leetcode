class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        nums: sorted asec
        target: number
        ''' 
        
        left, right = 0, len(nums)
        
        result = -1
        
        while left < right:
            
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            
            if target == nums[mid]:
                result = mid
                break
        return result
            