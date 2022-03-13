class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        r = c = 0
        is_row = False
        sign = 1
        turn = 0
        for i in range(1, n**2 + 1):
            print(r,c)
            mat[r][c] = i
            if is_row:
                r += sign
            else:
                c += sign
            
            
            if not((0 <= r < n) and (0 <= c < n)) or mat[r][c]:
                turn += 1
                
                
                if is_row:
                    r -= sign
                    if turn == 2:
                        turn = 0
                        sign = - sign
                    c += sign
                else:
                    c -= sign
                    if turn == 2:
                        turn = 0
                        sign = - sign
                    r += sign
                
                is_row = not is_row
                
                
                
                
                
                
                
            
            
            
        return mat
            
            
            