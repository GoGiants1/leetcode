class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        z_r = set()
        z_c = set()

        for i, row in enumerate(matrix):
            for j, el in enumerate(row):
                if el == 0:
                    z_r.add(i)
                    z_c.add(j)

        for i, row in enumerate(matrix):
            if i in z_r:
                matrix[i] = [0] * len(matrix[0])
                continue
            for j, el in enumerate(row):
                if j in z_c:
                    matrix[i][j] =0
        