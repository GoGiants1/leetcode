class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n 

        pref = [1] * (n+1)
        suff = [1] * (n+1)
        

        for i in range(n):
            pref[i+1] = pref[i] * nums[i]
            suff[-i-2] = suff[-1-i] * nums[-1-i]
        for i in range(n):
            out[i] = pref[i] * suff[i + 1]
        return out