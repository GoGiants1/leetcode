import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        # start from nums[0]
        # nums[i]: max jump length from index `i`
        
        # return minimun jumps to reach nums[n-1]
#         jumps = [None for _,_ in enumerate(nums)]
#         jumps[-1] = 0
#         def findJump(start: int):
#             if start == len(nums) -1:
#                 return 0
#             if jumps[start]:
#                 return jumps[start]
#             min_jump = math.inf
#             for step in range(nums[start], 0, -1):
#                 if step >= len(nums) - start:
#                     jumps[start] = 1
#                     return 1
#                 min_jump = min(1 + findJump(step + start), min_jump)
#             jumps[start] = min_jump
#             return jumps[start]
        
#         return findJump(0)
        # The starting range of the first jump is [0, 0]
    
        ### Greedy ####
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0
        
        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            cur_far = max(cur_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == cur_end:
                answer += 1
                cur_end = cur_far
                
        return answer