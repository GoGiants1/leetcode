class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            I have unlimited gas tank in my car. we travel clock-wise.
            start with empty gas at one of the gas station.
            
            Args:
                gas: list of integer
                    gas[i]: i^th station's gas amount
                
                cost: list of integer
                    cost[i]: amount of gas to travel i -> i + 1 gas station
            
            느낀점: 출발지가 유일하기 때문에 출발이 가능한지만 체크하면 되는 것이었다.
                            
        """
        """Brute Force
        
        n = len(gas)
        remain_gas = [gas[i] - cost[i] for i in range(n)]
        
        if sum(remain_gas) < 0:
            return -1
        
        start = -1
        for i, r in enumerate(remain_gas):
            gas_state = 0
            if r < 0:
                continue
            
            for j in range(0, n + 1):
                next_station = (i + j) % n
                gas_state += remain_gas[next_station]
                if gas_state < 0:
                    break
            
            if gas_state >= 0:
                start = i
        
        return start
        
        """
        """ O(N^2)
        n = len(gas)
        start = -1
        for i, (s, c) in enumerate(list(zip(gas,cost))):
            if s - c < 0:
                continue
            
            my_tank = 0
            for j in range(n):
                this_station = (i + j) % n
                my_tank += gas[this_station] - cost[this_station]
                if my_tank < 0:
                    break
            
            if my_tank >= 0:
                start = i
                break
    
        return start
        """
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start