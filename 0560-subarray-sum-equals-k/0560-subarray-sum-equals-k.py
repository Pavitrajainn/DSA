class Solution(object):
    def subarraySum(self, nums, k):
      n = len(nums)
      pre = []
      count = 0
      dic = {}
      pre.append(nums[0])
      for i in range(1,n):
        pre.append( pre[i-1] + nums[i] )
      for j in range(0,n):
        value = pre[j] - k
        if value == 0 :
            count += 1
        if value in dic :
          count = count + dic[value]
        dic[pre[j]] = dic.get(pre[j],0)+1
      return count  