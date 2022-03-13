class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # # (x, y, radius)
        # # O(N^2)
        # import heapq as hq
        # bomb_dict = defaultdict(list)
        # graph = defaultdict(set)
        # distance = {}
        
        # for i, v in enumerate(bombs):
        #     hq.heappush(bomb_dict[(v[0],v[1])], -v[2])
            
        # def checkRange(b1:(int,int,int), b2:(int,int,int)):
        #     x, y, r1 = b1
        #     a, b, r2 = b2
            
        #     dist = pow((x-a), 2) + pow((y-b), 2)
        #     if pow(r1,2) >= dist:
        #         graph[(x,y)].add((a,b))
        #     if pow(r2,2) >= dist:
        #         graph[(a,b)].add((x,y))

        # for i, v in enumerate(bomb_dict):
        #     for j, w in enumerate(bomb_dict):
        #         if i == j:
        #             continue
        #         checkRange((*v, -bomb_dict[v][0]), (*w, -bomb_dict[w][0]))
        
        # def detonate(x:int, y:int)->int:
            
        #     q = deque()
        #     q.append((x,y))
        #     detonated = set()
        #     count = 0
        #     while q:
        #         nxt = q.popleft()
        #         if nxt not in detonated:
        #             count += len(bomb_dict[nxt])
        #             detonated.add(nxt)
        #         else:
        #             continue

        #         for i, v in enumerate(graph[nxt]):
        #             if v not in detonated:
        #                 q.append(v)
        #     return count
        
        
        # max_count = -1

        # for i, v in enumerate(bomb_dict):
        #     max_count = max(detonate(*v), max_count)
        # return max_count
        graph = collections.defaultdict(list)
        n = len(bombs)
        
        # Build the graph
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue         
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Create a path from node i to node j, if bomb i detonates bomb j.
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        # DFS to get the number of nodes reachable from a given node cur
        def dfs(cur, visited):
            visited.add(cur)
            for neib in graph[cur]:
                if neib not in visited:
                    dfs(neib, visited)
            return len(visited)
        
        answer = 0
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))
        
        return answer