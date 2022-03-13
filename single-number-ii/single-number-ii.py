class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counts = [set() for _ in range(3)]


        for i, v in enumerate(nums):
            if v in counts[0]:
                counts[1].add(v)
                counts[0].remove(v)
            elif v in counts[1]:
                counts[2].add(v)
                counts[1].remove(v)
            elif v in counts[2]:
                continue
            else:
                counts[0].add(v)
        
        return counts[0].pop()
