class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # My Sol: Stack
        # st = []
        # out = []
        # for i, v in enumerate(nums):
        #     if st and st[-1] - v != -1:
        #         if len(st) == 1:
        #             out.append(str(st[-1]))
        #         else:
        #             out.append(f"{st[0]}->{st[-1]}")
        #         st.clear()
        #     st.append(v)
        # if st:
        #     if len(st) == 1:
        #         out.append(str(st[-1]))
        #     else:
        #         out.append(f"{st[0]}->{st[-1]}")
        # return out
        ranges = []     
        i = 0 
        
        while i < len(nums): 
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            if start != nums[i]: 
                ranges.append(str(start) + "->" + str(nums[i]))
            else: 
                ranges.append(str(nums[i]))
            
            i += 1

        return ranges