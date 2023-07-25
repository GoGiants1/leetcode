class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def findPeak(lo: int, hi: int):
            mid = (lo + hi) // 2
            print(lo, hi, mid)
            if lo < hi:
                if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                    return mid
                if arr[mid - 1] > arr[mid]:
                    hi = mid
                else:
                    lo = mid + 1

                return findPeak(lo, hi)
            else:
                return None
        
        return findPeak(0, len(arr) - 1)
            