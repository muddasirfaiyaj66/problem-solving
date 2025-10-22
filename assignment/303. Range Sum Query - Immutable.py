class NumArray(object):
    def __init__(self, nums):
        self.prefix = []
        cur = 0
        for i in nums:
            cur += i
            self.prefix.append(cur)

    def sumRange(self, left, right):
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum



sol = NumArray([-2, 0, 3, -5, 2, -1])
print(sol.sumRange(0, 2))  
print(sol.sumRange(2, 5))  
print(sol.sumRange(0, 5))  
