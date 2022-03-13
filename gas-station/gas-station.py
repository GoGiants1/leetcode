class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(gas) - sum(cost) < 0:
            return -1
        tank = 0
        start = 0
        for i in range(n):
            if tank < 0:
                tank = 0
                start = i
            tank += gas[i] - cost[i]

        return start