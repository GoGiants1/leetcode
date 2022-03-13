class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q = []
        z = []
        length = len(nums)        
        for n in nums:
            if n:
                q.append(n)
            else:
                z.append(n)
        nums[:] = q + z