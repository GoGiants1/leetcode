class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         set1 = set(nums1)
#         set2 = set(nums2)
        
#         inter = set1 & set2
#         inter_list = []
#         for v in inter:
#             a, b = nums1.count(v), nums2.count(v)
#             a = min(a,b)
#             if a > 0:
#                 inter_list.extend([v] * a)
#         return inter_list

        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        
        c1 = c1 & c2
        return c1.elements()