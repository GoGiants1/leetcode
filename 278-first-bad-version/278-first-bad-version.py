# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
                
            
            ml = isBadVersion(mid)
            mr = isBadVersion(mid + 1)

            if ml & mr is True:
                right = mid 
            elif ml | mr is False:
                left = mid + 1
            else:
                return mid + 1
        return 1 # case n=1
            
        
