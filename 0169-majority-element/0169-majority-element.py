class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        
        cnt = Counter(nums)
        
        a,b = cnt.most_common(1)[0]
        return a