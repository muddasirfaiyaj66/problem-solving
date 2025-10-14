class Solution(object):
    #[rob1,rob2,n,n+1,.....]
    def rob(self, nums):
        rob1,rob2=0,0
        for n in nums:
            temp=max(n +rob1, rob2)
            rob1=rob2
            rob2=temp
        return rob2

solution = Solution()

arr1=[1,2,3,1]
arr2=[2,7,9,3,1]

print(solution.rob(arr1))
print(solution.rob(arr2))