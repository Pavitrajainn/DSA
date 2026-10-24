class Solution(object):
    def findSubarrays(self, nums):
        n = len(nums)
        hash = []
        for i in range(0,n-1):
            value = nums[i] + nums[i+1]
            if value in hash:
                return True
            else:
                hash.append(value)
        return False