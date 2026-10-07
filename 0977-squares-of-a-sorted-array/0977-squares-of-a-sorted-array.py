class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
      n = len(nums)
      for i in range(0,n):
        nums[i] = nums[i] ** 2
      return(sorted(nums))
    #   min = [nums[i]]
    #   a = num[i]
    #   for i in range(0,n):
    #    for j in range(i+1,n):
    #     if nums[min] > num[i]:
    #         min = 