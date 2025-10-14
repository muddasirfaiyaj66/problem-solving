class Solution(object):
    
    # class Solution(object):
    # def canCompleteCircuit(self, gas, cost):
    #     totalGas = 0
    #     totalCost = 0
    #     start = 0
    #     currentGas = 0

    #     for i in range(len(gas)):
    #         totalGas+=gas[i]
    #         totalCost+=cost[i]
    #         currentGas += gas[i] - cost[i]
            
    #         if currentGas < 0:
    #             start = i + 1
    #             currentGas = 0

    #     return -1 if totalGas < totalCost else start
           
    def canCompleteCircuit(self, gas, cost):
        totalGas = sum(gas)
        totalCost = sum(cost)
        start = 0
        currentGas = 0

        if totalGas < totalCost:
            return -1

        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            
            if currentGas < 0:
                start = i + 1
                currentGas = 0

        return start


solution = Solution()

case_1_Gas = [1, 2,3, 4, 5]
case_1_Cost = [3, 4, 5, 1,2]
case_2_Gas = [2, 3, 4]
case_2_Cost = [3, 4, 3]

print(solution.canCompleteCircuit(case_1_Gas, case_1_Cost))
print(solution.canCompleteCircuit(case_2_Gas, case_2_Cost))
