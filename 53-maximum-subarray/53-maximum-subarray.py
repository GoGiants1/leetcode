class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dac(l, r):
            '''
            head_sum: maximum sum if we start adding from head
            tail_sum: maximum sum if we start adding from tail
            sum_: total sum of this section
            max_sum: maximum sum we have seen so far anywhwere
            '''
            
            if l == r: # base case
                return nums[l], nums[l], nums[l], nums[l]
            
            mid = (l+r)//2
            
            # find the values for left and right section
            head_sum_l, tail_sum_l, sum_l, max_sum_l = dac(l, mid)
            head_sum_r, tail_sum_r, sum_r, max_sum_r = dac(mid+1, r)
            
            # head_sum is maximum of head_sum left or entire sum of left array + head_sum right
            head_sum = max(head_sum_l, sum_l+head_sum_r)
            
            # tail_sum is maximum of tail_sum right or tail_sum left + sum of entire right array
            tail_sum = max(tail_sum_r, tail_sum_l+sum_r)
            
            # sum_ is just sum of left and right
            sum_ = sum_l+sum_r
            
            # max_sum is either max_sum seen so far on left or right or the middle (tail of left and head of right)
            max_sum = max(max_sum_l, max_sum_r, tail_sum_l+head_sum_r)
            
            return head_sum, tail_sum, sum_, max_sum
        
        _, _, _, max_sum = dac(0, len(nums)-1)
        return max_sum
    
            
            
                
        