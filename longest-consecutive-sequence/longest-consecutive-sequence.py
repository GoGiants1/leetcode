class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        visited = set()
        lon = -1
        if len(nums) <= 1:
            return len(nums)
        for v in nums:
            s.add(v)
        
        for k in s:
            if k in visited:
                continue
            else:
                l = r = k
                while l in s:
                    visited.add(l)
                    l -= 1
                while r in s:
                    visited.add(r)
                    r += 1
                
                lon = max(lon, r - l + 1 - 2)
            
        return lon

