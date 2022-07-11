class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        fewSoFar = [float('inf') for i in range(amount + 1)]
        fewSoFar[0] = 0
        
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount and fewSoFar[i] != float('inf'):
                    fewSoFar[i + coin] = min(fewSoFar[i + coin], 1 + fewSoFar[i])
                    
        return fewSoFar[amount] if fewSoFar[amount] != float('inf') else -1