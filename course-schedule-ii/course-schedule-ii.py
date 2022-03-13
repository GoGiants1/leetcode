class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        indegree = [0] * numCourses
        g = defaultdict(list)
        for crs, pre in prerequisites:
            indegree[crs] += 1
            g[pre].append(crs)
        q = deque()
        t_sort = []
        # using q
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            crs = q.popleft()
            t_sort.append(crs)
            for nxt in g[crs]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return t_sort if len(t_sort) == numCourses else []
