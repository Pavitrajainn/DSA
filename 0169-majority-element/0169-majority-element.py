class Solution: # this is solve by moore's algorithm
    def majorityElement(self, nums: list[int]) -> int:
        count = 1
        res = 0
        for i in range(0,len(nums)):
            if nums[i] == nums[res] :
                count += 1
            else:
                count -= 1
            if count == 0:
                count += 1
                res = i
        return nums[res]