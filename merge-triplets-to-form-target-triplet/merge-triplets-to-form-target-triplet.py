class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # d = {
        #     0: set(),
        #     1: set(),
        #     2: set()
        # }
        # for i, t in enumerate(triplets):
        #     ok = True
        #     for j, val in enumerate(t):
        #         if val > target[j]:
        #             ok = False
        #     if ok:
        #         d[0].add(t[0])
        #         d[1].add(t[1])
        #         d[2].add(t[2])
        
        # return target[0] in d[0] and target[1] in d[1] and target[2] in d[2]

        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3