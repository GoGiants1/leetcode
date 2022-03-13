class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#         def compare_and_insert(nums1, cur, a, b):
#             if a < b:
#                 nums1[cur] = a
#                 return True
#             else:
#                 nums1[cur] = b
#                 return False
#         i = j = 0
#         cur = 0
#         org = nums1[:]
#         is_org = False
#         while cur < m+n:
            
#             if not j < n:
#                 is_org = compare_and_insert(nums1, cur, org[i], float('inf'))
#             elif not i< m:
#                 is_org = compare_and_insert(nums1, cur, float('inf'), nums2[j])
#             else:
#                 is_org = compare_and_insert(nums1, cur, org[i], nums2[j])
#             cur += 1
#             if is_org:
#                 i += 1
#             else:
#                 j += 1

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        
            
    