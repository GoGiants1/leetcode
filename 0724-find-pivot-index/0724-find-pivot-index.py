class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_s = 0
        r_s = sum(nums[1:])
        if r_s == l_s:
                return 0
        n = len(nums)
        for i in range(1, n):
            l_s += nums[i - 1]
            r_s -= nums[i]
            if r_s == l_s:
                return i
        return -1