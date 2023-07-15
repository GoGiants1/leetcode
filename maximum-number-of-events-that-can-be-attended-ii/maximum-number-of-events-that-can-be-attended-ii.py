class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()
        @cache
        def dp(curr: int, remain: int)->int:
            if remain == 0:
                return 0
            if curr >= n:
                return 0
            out = []
            nxt = curr + 1
            while nxt < n and events[nxt][0] <= events[curr][1]:
                nxt += 1
            return max(dp(curr + 1, remain), dp(nxt, remain - 1) + events[curr][2])
        
        return dp(0, k)

