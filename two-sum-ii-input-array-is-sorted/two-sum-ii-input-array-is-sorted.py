class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # 감소 x, 정렬
        # from bisect import bisect

        # lo, hi = 0, len(numbers)

        # while lo < hi:
        #     hi = bisect(numbers, target - numbers[lo])
        #     if numbers[hi-1] + numbers[lo] == target:
        #         return [lo + 1, hi]
        #     else:
        #         lo += 1
        
        # return [lo, hi]

        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1