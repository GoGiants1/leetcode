class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        n = len(nums)
        # n * two sum
        s = set()
        out = []
        for i in range(n-2):
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                sum2 = nums[l] + nums[r]
                if target > sum2:
                    l += 1
                elif target < sum2:
                    r -= 1
                else:
                    s.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        return [list(tp) for tp in s]
