class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        rng = set(i for i in range(n + 1))
        hash_set = set(nums)
        
        return list(rng - hash_set)[0]
        
        
        