class Solution:
    def numOfWays(self, num: List[int]) -> int:
        mod =10 ** 9 + 7
        
        def combination(nl, nr):
            return factorial[nl+nr] // factorial[nl] // factorial[nr]
            
        def ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            
            left = [num for num in arr if num < root]
            right = [num for num in arr if num > root]
            
            return ways(left) * ways(right) * combination (len(left), len(right))
            
        n = len(num)
        
        factorial = [1] * (n)
        
        for i in range (1,n):
            factorial[i] = factorial [i-1] * i
            
        return (ways(num)-1 ) % mod