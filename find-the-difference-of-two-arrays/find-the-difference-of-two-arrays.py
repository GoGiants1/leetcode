class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        s_1 = set(nums1)
        s_2 = set(nums2)

        a = s_1 - s_2
        b = s_2 - s_1

        return [list(a), list(b)]