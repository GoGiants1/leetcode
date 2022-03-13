class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = collections.defaultdict(int)
        
        for n in nums:
            if cnt[n] == 0:
                cnt[n] = nums.count(n)
            
            if cnt[n] > len(nums) // 2:
                return n