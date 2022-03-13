class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def jump(pos: int):
            if pos + nums[pos] >= n - 1:
                return True
            else:
                out = False
                for i in range(1,nums[pos]+1):
                    out |= jump(pos + i)
                    if out:
                        break
                return out
            
        return jump(0)
