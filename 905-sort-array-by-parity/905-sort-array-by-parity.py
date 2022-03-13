class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
#         even = []
        
#         odd = []
        
#         for n in nums:
#             if n % 2:
#                 odd.append(n)
#             else:
#                 even.append(n)
                
        
#         return even + odd

        # nums.sort(key = lambda x: x % 2)
        # return nums
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A