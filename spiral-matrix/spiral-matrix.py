class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direc = [(0,1), (1,0), (0, -1), (-1,0)]

        start = (0, 0)
        visited = set()
        visited.add((0,0))
        self.out = [matrix[0][0]]
        def visit(pos: list[int, int], prev_dir: int )->int:
            
            for i in range(prev_dir, prev_dir + 4):
                dr, dc = direc[i % 4]
                r = pos[0] + dr
                c = pos[1] + dc
                if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
                    continue
                if (r, c) in visited:
                    continue
                else:
                    visited.add((r,c))
                    self.out.append(matrix[r][c])
                    visit((r,c), i)
        visit((0,0), 0)        
        return self.out
        