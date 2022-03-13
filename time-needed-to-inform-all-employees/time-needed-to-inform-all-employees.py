class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                graph[v].append(i)
        
        q = deque()
        q.append((headID,0))
        max_mnt = -1
        while q:
            me, mnt = q.popleft()
            if me not in graph:
                max_mnt = max(max_mnt, mnt)
            for v in graph[me]:
                q.append((v, mnt + informTime[me]))
        return max_mnt
