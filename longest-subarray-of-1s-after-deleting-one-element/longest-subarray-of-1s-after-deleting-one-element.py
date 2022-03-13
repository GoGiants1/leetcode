class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # sliding window
        n = len(nums)
        z_cnt = 0
        l = 0
        mx = 0
        for r in range(n):
            if nums[r] != 1:
                if z_cnt == 0:
                    z_cnt += 1
                else:
                    while z_cnt > 0:
                        if nums[l] == 0:
                            z_cnt -= 1
                        l += 1
                    z_cnt += 1
            mx = max(mx, r - l)

        return mx