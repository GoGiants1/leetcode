class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        arrow = '->'
        out = []   
        def makeRange(l: int, u: int):
            inter = u - l
            if inter == 0:
                out.append(f"{l}")
            elif inter >=1 :
                out.append(f"{l}"+ arrow + f"{u}")
                
        if len(nums) == 0:
            makeRange(lower, upper)
            return out
        
        makeRange(lower ,nums[0] - 1)
        
        
        for i in range(len(nums) - 1):
            makeRange(nums[i] + 1, nums[i+1] -1)
        
        makeRange(nums[-1] + 1, upper)
            
        return out