class Solution(object):
    def missingNumber(self, nums):
       n = len(nums)+1
       arr = [0]*n
       for i in nums:
          arr[i] =  1
       for i in range(0,n):
          if arr[i] == 0:
            return i
        

        