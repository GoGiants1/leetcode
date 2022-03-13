class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(path: list[int], remain: set)-> list:
            if len(path) == len(nums):
                out.append(path)

                return
            r_copy = remain.copy()
            for r in remain:
                r_copy.remove(r)
                path.append(r)
                permutation(path[:], r_copy)
                path.pop()
                r_copy.add(r)

            return
        
        out = []
        permutation([], set(nums))
        return out