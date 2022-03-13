class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        q = deque()
        cnt = 0
        for i, v in enumerate(nums):
            if v == val:
                q.append(i)
                nums[i] = 0
                cnt += 1
            else:
                if len(q):
                    idx = q.popleft()
                    nums[idx] = v
                    q.append(i)

        return len(nums) - cnt