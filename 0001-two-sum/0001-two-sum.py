class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        hash = {}
        for i in range(0,n):
          value  = target - nums[i]
          if  value in hash:
            return (hash[value],i)
          else:
            hash[nums[i]] = hash.get(nums[i],i)
            
      
        