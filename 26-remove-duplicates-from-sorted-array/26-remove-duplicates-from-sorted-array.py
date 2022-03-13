class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            Returns:
                k: length of non-duplicated number list after remove duplicated numbers in nums list
                
            Approach: Use two pointer
        """
        n = len(nums)
        
        # if n == 1:
        #     return n
        # if n == 2:
        #     if nums[0] != nums[1]:
        #         return 2
        #     else:
        #         return 1
        
        l, r = 0, 1
        put_idx = 1
        
        while l < n:
            
            if r >= n:
                l += 1
                continue
            
            if nums[l] == nums[r]:
                r += 1
                continue
            
            else:
                nums[put_idx] = nums[r]
                put_idx += 1
                l = r
                r = l + 1
                
        if put_idx == 0:
            return 1

        elif put_idx < n and nums[put_idx - 1] != nums[l-1]:
            put_idx += 1
        
        return put_idx