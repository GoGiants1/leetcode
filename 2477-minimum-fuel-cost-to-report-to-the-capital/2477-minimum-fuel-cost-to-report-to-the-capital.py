class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        rd = defaultdict(list)
        if len(roads) == 0:
            return 0
        for u, v in roads:
            rd[u].append(v)
            rd[v].append(u)
        visit = set()
        # return : peoples, fuels
        def dfs(city: int) -> (int, int):
            if city not in rd:
                return (1, 1)
            visit.add(city)
            peoples = fuels = 0 
            for nxt in rd[city]:
                if nxt not in visit:
                    pp, f = dfs(nxt)
                    peoples += pp
                    fuels += f
            
            if city == 0:
                return peoples, fuels
            
            peoples += 1
            cars, remain = divmod(peoples, seats)
            if remain > 0:
                cars += 1
                
            return peoples, fuels + cars
    
        _, out = dfs(0)
        
        return out