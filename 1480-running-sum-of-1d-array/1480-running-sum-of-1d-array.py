class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      runingsum= [0] * len(nums)
      runingsum[0] = nums[0]
      for i in range(1,len(nums)):
        runingsum[i] = runingsum[i-1] + nums[i]
      return  runingsum