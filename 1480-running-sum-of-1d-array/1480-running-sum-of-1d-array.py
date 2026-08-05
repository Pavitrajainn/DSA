class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      sum = 0
      runingsum =[]
      for i in range(len(nums)):
         sum += nums[i]
         runingsum.append(sum)
      return  runingsum