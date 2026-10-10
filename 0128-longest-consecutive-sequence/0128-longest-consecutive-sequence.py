class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        large = float("-inf")
        count = 0
        max_count = 0
        for i in range(0,n):
            if nums[i] -1 == large:
                count += 1
            elif nums[i] != large :
                count = 1
            large = nums[i]
            max_count = max(max_count , count)
        return max_count  
                 
