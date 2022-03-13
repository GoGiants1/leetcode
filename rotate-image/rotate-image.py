class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 90도 시계방향 회전

        n = len(matrix)


        layer_size = n

        direc = [(1, 0), (0, -1), (-1,0)]
        def swap(layer: int):
            x, y = layer, layer
            xx, yy = layer, n - 1 -layer

            if n - 2 * layer <= 1:
                return
            
            for i in range(3):
                x, y = layer, layer
                dx, dy = direc[i]
                for _ in range(n-1-layer*2):
                    matrix[x][y], matrix[xx][yy] = matrix[xx][yy], matrix[x][y]
                    xx += dx
                    yy += dy
                    y += 1
            swap(layer + 1)
        swap(0)



