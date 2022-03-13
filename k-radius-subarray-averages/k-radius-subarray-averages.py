class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        out = []
        t = 2 * k + 1
        if len(nums) < t:
            return [-1] * len(nums)
        cnt = 0
        s = 0
        for i, v in enumerate(nums):
            if cnt < t:
                cnt += 1
                s += v
            else:
                out.append(s//t)
                s += v - nums[i - t]
        if cnt == t:
            out.append(s // t)
                
        return [-1] * k + out + [-1] * k