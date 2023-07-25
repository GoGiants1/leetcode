class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def findPeak(lo: int, hi: int):
            mid = (lo + hi) // 2
            if lo < hi:
                if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                    return mid
                l = findPeak(lo, mid)
                if l:
                    return l
                else:
                    return findPeak(mid + 1, hi)
            else:
                return None
        
        return findPeak(0, len(arr) - 1)
            