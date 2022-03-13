class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        d = collections.defaultdict(int)
        
        for n in nums:
            d[n] += 1
        
        keys = list(d.keys())
        ret = 0
        
        for n in keys:
            
            n_k = k - n
            
            while d[n] > 0 and d[n_k] > 0:
                d[n] -= 1
                d[n_k] -= 1
                if d[n_k]>=0 and d[n]>=0:  
                    ret += 1
                else:
                    d[n] += 1
                    d[n_k] += 1
                    break
            
        return ret