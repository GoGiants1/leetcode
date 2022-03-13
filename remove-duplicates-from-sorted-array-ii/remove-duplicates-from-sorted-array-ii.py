class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # two pass
        cnt = 0
        prev = nums[0]
        q = deque()
        delete_cnt = 0
        
        for i, v in enumerate(nums):
            if prev == v:
                cnt += 1
                if cnt > 2:
                    q.append(i)
                    delete_cnt += 1
                    continue
            else:
                cnt = 1
                prev = v
            if q:
                insert = q.popleft()
                nums[insert] = v
                q.append(i)
        
        return len(nums) - delete_cnt
