class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for v in bin(n):
            if v == "1":
                cnt += 1
        return cnt