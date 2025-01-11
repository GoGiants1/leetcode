class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(start: int, path: list[int]):
            if start >= n:
                res.append(path.copy())
                return
            path.append(nums[start])
            dfs(start + 1, path)
            path.pop()
            dfs(start + 1, path)
        
        dfs(0, [])
        return res