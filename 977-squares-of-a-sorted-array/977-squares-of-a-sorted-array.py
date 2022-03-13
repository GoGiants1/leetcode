class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        q = collections.deque()
        
        l, r = 0, len(nums) - 1
        
        neg = collections.deque()
        pos = collections.deque()
        
        while l < len(nums) and nums[l] < 0:
            neg.append(nums[l])
            l += 1
    
        while nums[r] >= 0 and r >= 0:
            pos.append(nums[r])
            r -= 1
            
        # return neg, pos
        
        while neg or pos:
            if neg and pos:
                if neg[0] ** 2 > pos[0] ** 2:
                    q.appendleft(neg.popleft() ** 2)
                else:
                    q.appendleft(pos.popleft() ** 2)
            elif neg:
                q.appendleft(neg.popleft() ** 2)
            elif pos:
                q.appendleft(pos.popleft() ** 2)
                
        return list(q)