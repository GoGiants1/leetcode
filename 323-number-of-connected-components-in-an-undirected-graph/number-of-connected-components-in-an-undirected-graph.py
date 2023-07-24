class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def bfs(s: int):
            q = deque()
            q.append(s)
            while q:
                node = q.popleft()
                visit.add(node)

                for w in g[node]:
                    if w not in visit:
                        q.append(w)
        
        # do bfs for every node
        g = defaultdict(list)
        for k, v in edges:
            g[k].append(v)
            g[v].append(k)

        visit = set()
        cnt = 0
        for start in range(n):
            if start not in visit:
                bfs(start)
                cnt += 1

        
        

                
        return cnt