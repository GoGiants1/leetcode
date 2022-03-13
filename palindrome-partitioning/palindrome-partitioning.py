class Solution:
    def partition(self, s: str) -> List[List[str]]:
        from functools import cache
        from collections import defaultdict
        d = defaultdict(list)
        out = []

        @cache
        def checkPal(start:int, end:int):
            print(start, end)
            
            if start > end:
                return
            if start == end:
                d[start].append(s[start])
                return
            l, r = start, end
            is_pal = True
            while l < r:
                if s[l] != s[r]:
                    is_pal = False
                    break 
                else:
                    l += 1
                    r -= 1
            if is_pal is True:
                d[start].append(s[start:end+1])
            checkPal(start, end-1)
            checkPal(start+1, end)
        
        def backtrack(path:list, curr: int):
            
            if curr == len(s):
                out.append(path[:])
            
            for w in d[curr]:
                if curr + len(w) <= len(s):
                    path.append(w)
                    backtrack(path, curr + len(w))
                    path.pop()
            

        checkPal(0, len(s) - 1)
        backtrack([], 0)
        return out