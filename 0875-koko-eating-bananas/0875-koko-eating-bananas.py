class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k is eating speed (per hr)
        
        
        l, r = 1, max(piles)
        
        k = (l + r) // 2
        
        
        
        
        while l <= r:
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            
            if hrs > h:
                l = k + 1
            else:
                r = k - 1
            k = (l + r) // 2
        
        return l