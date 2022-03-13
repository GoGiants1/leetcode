class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()

        for i, v in enumerate(nums):
            if v in hs:
                return True
            hs.add(v)
        return False