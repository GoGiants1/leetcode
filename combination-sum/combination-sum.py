class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. sort candidates

        candidates.sort() # O(1)
        out = []
        # curr: path that sum(crr) <= target
        def makePath(curr:list, need: int, f_idx: int)-> None:
            if need < 0:
                return
            elif need == 0:
                out.append(curr[:])

            
            for i in range(f_idx, len(candidates)):
                if candidates[i] <= need:
                    curr.append(candidates[i])
                    makePath(curr, need - candidates[i], i)
                    curr.pop()
        makePath([], target, 0)
        return out