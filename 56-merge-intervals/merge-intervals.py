class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def checkMergable(l1: list, l2: list):
            if l1[0] > l2[1]:
                l1, l2 = l2, l1

            if l1[1] >= l2[0]:
                return True
            return False

        def mergeTwo(l1, l2):
            return [min(l1[0], l2[0]), max(l1[1], l2[1])]
            
        intervals.sort()
        out = []
        temp = intervals[0]
        for i, v in enumerate(intervals):
            if i == 0:
                continue
            if checkMergable(temp, v):
                temp = mergeTwo(temp, v)
            else:
                out.append(temp)
                temp = v
        if len(temp):
            out.append(temp)
        return out
