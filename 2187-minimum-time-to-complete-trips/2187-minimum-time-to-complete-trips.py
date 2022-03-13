class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # async trip to make up totalTrips
        # bin search
        m = min(time)
        l, r = 0, totalTrips * m
        
        while l != r:
            mid = (l + r) // 2
            
            acc = sum([mid // t for t in time])
            print(l, r, mid, acc)
            
            
            if acc < totalTrips:
                print('first')
                l = mid + 1
            elif acc > totalTrips:
                print('sec')
                r = mid
            else:
                while acc == totalTrips:
                    mid -= 1
                    acc = sum([mid // t for t in time])
                return mid + 1
        
        return l
        