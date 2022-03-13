class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_w = sum(weights)
        
        l = max(weights)
        r = total_w
        
        
        
        while l < r:
            mid = (r + l) // 2
            curr_loads = 0
            day = 0
        
            for i, v in enumerate(weights):
                if curr_loads + v <= mid:
                    curr_loads += v
                    continue
                else:
                    day += 1
                    curr_loads = v
                
            if day < days:
                r = mid
            else:
                l = mid + 1
            
        return r
                    
        