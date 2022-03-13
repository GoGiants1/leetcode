class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        high = 0
        prev = 0
        for i, v in enumerate(gain):
            prev += v
            high = max(prev, high)
        return high