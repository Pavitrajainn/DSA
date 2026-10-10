class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0 
        nums = sorted(nums)
        count = 1
        max_count = 1
        for i in range(0,n-1):
            if nums[i] == nums[i+1]:
                pass    
            elif nums[i]+1 == nums[i+1]:
                count += 1
                max_count = max(max_count , count)
            else:
                count = 1
        return max_count  
                 
