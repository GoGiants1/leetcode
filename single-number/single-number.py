class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0

        for i, v in enumerate(nums):
            acc ^= v
        
        return acc


        

