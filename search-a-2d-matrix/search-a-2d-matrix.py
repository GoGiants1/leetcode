class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m = len(matrix)
        # n = len(matrix[0])
        # from bisect import bisect_left
        # for i, row in enumerate(matrix):
        #     idx = bisect_left(row, target)
        #     if idx >= n:
        #         continue
        #     else:
        #         return row[idx] == target

        # return False

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False