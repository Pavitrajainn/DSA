class Solution(object):
    def pivotIndex(self, nums):
       n = len(nums)
       pre = []
       pre.append(nums[0])
       pre_total = 0
       for i in range(1,n):
         pre.append( pre[i-1] + nums[i] )
       total_sum = pre[n-1]
       for i in range(0,n):
         if total_sum - pre[i] == pre_total :
            return i
         pre_total = pre[i]
       return -1

