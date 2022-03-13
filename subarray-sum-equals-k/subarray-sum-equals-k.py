class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans , prefsum, d = 0,  0, {0:1}
        for num in nums:
            prefsum += num
            if  prefsum-k  in  d:
                ans = ans + d[prefsum-k]
            d[prefsum] = d.get(prefsum, 0) + 1
        return ans

