class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # make graph (numerator, denominator)
        vals = {}
        graph = collections.defaultdict(list)
        for i, (a, b) in enumerate(equations):
            if a != b:
                vals[(a, b)] = values[i]
                vals[(b, a)] = 1 / values[i]
                graph[a].append(b)
                graph[b].append(a)

        out = []
        def dfs(start: str, target: str, prev: str, acc: float,  visited:set)-> None:
            if prev not in graph:
                return 
            if prev == target:
                if (start, target) not in vals:
                    out.append(acc)
                    vals[(start, target)] = acc
                return

            for nxt in graph[prev]:
                if nxt not in visited:
                    v = vals[(prev, nxt)]
                    visited.add(nxt)
                    dfs(start, target, nxt, acc * v, visited)
                    visited.remove(nxt)
        visited = set()
        for j, q in enumerate(queries):
            n, dn = q
            if (n, dn) in vals:
                out.append(vals[(n,dn)])
            else:
                visited.add(n)
                dfs(n, dn, n, 1, visited)
                visited.remove(n)
            if len(out) == j:
                out.append(-1)

        return out