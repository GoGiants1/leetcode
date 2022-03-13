class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        jump = 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            jump += 1
    
        return jump


        # Sol 1. DP
        # n = len(nums)
        # if n <= 1:
        #     return 0
        # dp = [math.inf] * (n)
        # # state variable: jump count, idx
        # # recurrence relation
        # # dp(i) = min(dp(i-1) + 1, dp(i-2) + 1, ...)
        # dp[0] = 0
        # for i in range(n):
        #     for k in range(nums[i], 0, -1):
        #         if i+k < n:
        #             dp[i+k] = min(dp[i] + 1, dp[i+k])
        # return dp[-1]

        # Sol 2. BFS
        # n = len(nums)
        # q = deque()
        # q.append((0,0))
        # visited = set()

        # while q:
        #     now, jmp = q.popleft()
        #     if now >= n-1:
        #         return jmp
        #     for i in range(nums[now], 0, -1):
        #         if i + now not in visited:
        #             visited.add(i+now)
        #             q.append((now+i, jmp+1))
        # return 0


