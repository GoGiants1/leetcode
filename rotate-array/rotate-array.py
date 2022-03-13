class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n
        if k == 0:
            return

        q = deque()
        for i, v in enumerate(nums):
            q.append(v)
            if i < k:
                nums[i] = nums[n-k+i]
            else:
                if q:
                    nums[i] = q.popleft()
            
