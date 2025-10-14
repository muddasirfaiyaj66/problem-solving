'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''


'''
array = [3,2,1,0,4]
index :  0 1 2 3 4

maxIndex:3 3 3 3 (here we can maximum jump to at index 3 but here index is 4 so it not possible)
'''
class Solution(object):
    def canJump(self, nums):
       maxIndex=0
       
       for i in range(len(nums)):
           if i > maxIndex:
               return False
           maxIndex=max(maxIndex,i + nums[i])
           
       return True
   
   
solution =Solution()

test_case_1 =[2,3,1,1,4]
test_case_2 =[3,2,1,0,4]

print(solution.canJump(test_case_1))
print(solution.canJump(test_case_2))


