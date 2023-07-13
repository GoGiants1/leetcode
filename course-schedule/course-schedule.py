class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for (crs, pre) in prerequisites:
            indegree[crs] += 1
            graph[pre].append(crs)
        
        q = deque()
    
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        topological_order = []
        while q:
            course = q.popleft()
            topological_order.append(course)
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return len(topological_order) == numCourses