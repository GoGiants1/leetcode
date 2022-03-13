class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        ans = []
        for key, val in cnt.items():
            bucket[val].append(key)
        for i in range(n, 0, -1):
            if len(ans) == k:
                return ans
            if len(bucket[i]) > 0:
                ans.extend(bucket[i])
        return ans