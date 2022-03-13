class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # improved
        m, n = len(grid), len(grid[0])
        neg_cnt = 0
        # from bisect import bisect
        
        # while r < m:
        #     c = bisect(grid[r], 0, key=lambda x: -x)
        #     if c < n:
        #         neg_cnt += n - 1 - c + 1
        #     r += 1
        
        curr_idx = n - 1

        for row in grid:
            while curr_idx >= 0 and row[curr_idx] < 0:
                curr_idx -= 1
            
            neg_cnt += n - 1 - curr_idx

        return neg_cnt
        