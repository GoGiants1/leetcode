class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # 양방향, 가중치 있음
        # start, end 

        # Sol 2. SPFA
        # from math import log

        # graph = defaultdict(list)

        # for i, (v, w) in enumerate(edges):
        #     graph[v].append((w, succProb[i]))
        #     graph[w].append((v, succProb[i]))
        # max_prob = [0] * n
        # max_prob[start] = 1
        # mx = -math.inf
        # q = deque()

        # # node, prob
        # q.append(start)
        # while q:
        #     node = q.popleft()
        #     for nxt, p in graph[node]:
        #         if max_prob[nxt] < p * max_prob[node]:
        #             q.append(nxt)
        #             max_prob[nxt] = p * max_prob[node]
        
        # return max_prob[end]

        # Sol 2. Dijkstra Algorithm
        from heapq import heappush, heappop
        graph = defaultdict(list)

        for i, (v, w) in enumerate(edges):
            graph[v].append((w, succProb[i]))
            graph[w].append((v, succProb[i]))
        max_prob = [0] * n
        max_prob[start] = 1

        pq = []

        # node, prob
        heappush(pq, ((-1, start)))
        visited = set()
        while pq:
            prob, node = heappop(pq)
            if node == end:
                return - prob
            for nxt, p in graph[node]:
                if max_prob[nxt] < p * max_prob[node]:
                    max_prob[nxt] = p * max_prob[node]
                    heappush(pq, (-max_prob[nxt], nxt))
            visited.add(node)
        return max_prob[end]