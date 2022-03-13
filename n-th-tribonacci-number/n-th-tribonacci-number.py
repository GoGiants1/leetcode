class Solution:
    def tribonacci(self, n: int) -> int:
        tab = [0] *( n + 1)
        if n <= 1:
            return n
        if n == 2:
            return 1
        tab[0:3] = [0,1,1]
        for i in range(3, n+1):
            tab[i] = tab[i-1] + tab[i-2] + tab[i-3]
            
        return tab[-1]