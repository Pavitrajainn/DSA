class Solution(object):
    def sortColors(self, nums):
     n = len(nums)
     for i in range(n-2,-1,-1):
        remove_flg = False
        for j in range(0,i+1):
            if nums[j] >= nums[j+1] :
                nums[j] , nums[j+1] = nums[j+1] , nums[j] 
                remove_flg = True
        if not remove_flg:
            break