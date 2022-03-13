class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # locations 

        # base case
        # 1. fuel < 0
        
        # tabulation
        # fuel > 0 and at fin
        # state: fuel and idx
        n = len(locations)
        @cache
        def travel(f: int, pos:int):
            if f < 0:
                return 0
            else:
                out = 0 if pos != finish else 1
                for i in range(n):
                    if i == pos:
                        continue
                    out += travel(f - abs(locations[i] - locations[pos]), i)
                return out
        return travel(fuel, start) % (10 ** 9 + 7)