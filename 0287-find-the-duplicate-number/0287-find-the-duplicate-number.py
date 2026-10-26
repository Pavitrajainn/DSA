class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hash = {}
        n = len(nums)
        for i in nums:
            hash[i] = hash.get(i,0)+1
        for i in hash:
            if hash[i] >= 2:
                return i