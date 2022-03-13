class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # BFS
        
#         visited = []
        
#         stack = [source]
        
#         graph = defaultdict(list)
#         edges.sort()
#         for i,(v, w) in enumerate(edges):
#             graph[v].append(w)
#             graph[w].append(v)
        
#         while stack:
#             node = stack.pop()            
#             for i, nxt in enumerate(graph[node]):
#                 if nxt == destination:
#                     return True
#                 elif nxt not in visited:
#                     stack.append(nxt)
#             visited.append(node)
            
#         return True if destination in visited else False
        # DFS
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = [False] * n
        
        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)