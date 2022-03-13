class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        cnt_s = Counter(s)
        cnt_goal = Counter(goal)
        def findDiffIdx(start: int)->int:
            curr = start
            while curr < len(s) and s[curr] == goal[curr]:
                curr += 1
            return curr
        if cnt_s != cnt_goal:
            return False
        if s == goal:
            if cnt_s.most_common(1)[0][1] >= 2:
                return True
            else:
                return False
        
    
        i = findDiffIdx(0)
        j = findDiffIdx(i+1)
        last = findDiffIdx(j+1)
        if last < len(s):
            return False
        else:
            return True