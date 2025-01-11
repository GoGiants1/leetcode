class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(start: int, comb: list[int], partial_sum: int):
            if start >= len(candidates):
                if partial_sum == target:
                    res.append(comb[:])
                return
            if partial_sum > target:
                return
            comb.append(candidates[start])
            dfs(start, comb, partial_sum + candidates[start])
            comb.pop()
            dfs(start + 1, comb, partial_sum)

        dfs(0, [], 0)
        return res