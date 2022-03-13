class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        # acc = reduce(lambda x, cur: cur * x, nums, 1)

        # if acc == 0:
        #     return 0
        # elif acc > 0:
        #     return 1
        # else:
        #     return -1
        cnt_neg = 0
        for i, v in enumerate(nums):
            if v == 0:
                return 0
            if v < 0:
                cnt_neg += 1
        
        if cnt_neg % 2 == 1:
            return -1
        else:
            return 1