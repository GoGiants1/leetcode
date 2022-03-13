class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = collections.defaultdict(list)
        for i, num in enumerate(numbers, 1):
            w = target - num
            if w in d.keys():
                if len(d[w]):
                    return sorted([ *d[w] , i ])

            d[num].append(i)
            