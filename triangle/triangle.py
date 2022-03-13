class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # base case => bottom triangle arr
        # depth and idx (state)
        
        @cache
        def dp(depth: int, idx: int):
            if depth == len(triangle) - 1:
                if idx < len(triangle[depth]):
                    return triangle[depth][idx]
                else:
                    return math.inf

            return min(dp(depth + 1, idx), dp(depth + 1, idx + 1)) + triangle[depth][idx]

        return dp(0,0)