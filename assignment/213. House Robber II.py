class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helperRob(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        skipFirstHouse = nums[1:]
        skipLastHouse = nums[:-1]
        
        return max(helperRob(skipFirstHouse), helperRob(skipLastHouse))


solution = Solution()
print(solution.rob([2,3,2]))      
print(solution.rob([1,2,3,1]))    
print(solution.rob([1,2,3]))      