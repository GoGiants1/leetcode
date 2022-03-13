class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        hs = set()
        def backtrack(path:list[int], idx: int):
            t = tuple(path)
            if t in hs:
                return 
            else:
                hs.add(t)
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()

        backtrack([], 0)
        return list(hs)