class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        nums.append(-math.inf)
        nums.append(-math.inf)

        def bin_search(lo:int, hi: int):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            else:
                l = bin_search(lo, mid - 1)
                if l is not None:
                    return l
                r = bin_search(mid + 1, hi)
                if r is not None:
                    return r
                return None

        return bin_search(l, r)