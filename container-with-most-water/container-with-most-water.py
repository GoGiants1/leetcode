class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Container With Most Water
        n = len(height)
        l, r = 0, n-1
        m = 0
        while l < r:
            l_h = height[l]
            r_h = height[r]

            if l_h > r_h:
                m = max(r_h * (r-l), m)
                r -= 1
            else:
                m = max(l_h * (r-l), m)
                l += 1
        return m