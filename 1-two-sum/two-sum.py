class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map
        from collections import defaultdict       
        nums_dict = defaultdict(list)

        for i, v in enumerate(nums):
            nums_dict[v].append(i)

        for k in nums_dict.keys():
            pair = target - k
            if pair in nums_dict:
                if pair != k:
                    return [nums_dict[k][0], nums_dict[pair][0]]
                else:
                    if len(nums_dict[k]) >= 2:
                        return nums_dict[k][:2]
        return []            