class Solution(object):
    def findDuplicate(self, nums):
       nums.sort()
       n = len(nums)
       target = nums[0]
       count = 1
       for i in range(1,n):
         if target == nums[i]:
             count += 1
         else:
             count -= 1
         if count == 0:
             count = 1
             target = nums[i]
         if count > 1:
             return nums[i]
       