class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.d = {}
        def makeSubSet(n: list[int]):
            t = tuple(n)
            if t in self.d:
                return 
            else:
                self.d[t] = n
            for i, v in enumerate(n):
                makeSubSet(n[:i] + n[i+1:])
        makeSubSet(nums)
        return list(self.d.values())