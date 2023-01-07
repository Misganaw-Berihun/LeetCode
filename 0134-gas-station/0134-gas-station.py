class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        gas_in_tank = sum(gas)
        gas_required = sum(cost)
        start_index = -1
        
        if gas_in_tank >= gas_required:
            start_index = 0
            cur_gas = 0
            
            for i in range(size):
                cur_gas += (gas[i] - cost[i]) 
                
                if cur_gas < 0:
                    start_index = (i + 1)
                    cur_gas = 0
        
        return start_index
        