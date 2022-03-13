class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:


        def calcGrad(i:int):
            dy = (coordinates[i][1] - coordinates[i-1][1])
            dx = (coordinates[i][0] - coordinates[i-1][0])
            if dx == 0:
                return math.inf
            else:
                return dy / dx

        
        self.grad = calcGrad(0)
        
        for i in range(1, len(coordinates)):
            grad = calcGrad(i)

            if grad != self.grad:
                return False

        return True