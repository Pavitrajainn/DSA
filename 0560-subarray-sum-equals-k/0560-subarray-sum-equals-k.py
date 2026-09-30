class Solution(object):
    def subarraySum(self, nums, k):
      n = len(nums)
      count = 0
      pre =[]
      hash ={}
      pre.append(nums[0])

      for i in range(1,n):
        pre.append(pre[i-1] + nums[i])

      for i in range(0,n):
        if pre[i] == k:
            count += 1

        value = pre[i] - k

        if value in hash:
            count += hash[value]

        hash[pre[i]] = hash.get(pre[i],0) + 1

      return count    
