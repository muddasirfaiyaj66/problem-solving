class Solution(object):
    def coinChange(self, coins, amount):
        dp =[float('inf')] * (amount +1)
        dp[0]=0
        
        for coin in coins:
            for curr_amount in range (coin,amount +1):
                dp[curr_amount] = min(dp[curr_amount],dp[curr_amount - coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
    
    

sol = Solution()
print(sol.coinChange([1, 2, 5], 11))  
print(sol.coinChange([2], 3))         
print(sol.coinChange([1], 0))  