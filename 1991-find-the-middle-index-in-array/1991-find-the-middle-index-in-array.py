class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
       n = len(nums)
       total = 0  
       pre = []
       pre.append(nums[0])
       for i in range(1,n):
         pre.append(pre[i-1] + nums[i])
       pre_sum = pre[n-1]
       for i in range(0,n):
        if pre_sum - pre[i] == total:
            return i
        total = pre[i]
       return -1

         