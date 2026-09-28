class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash = {}
        max_fac = 0
        for i in nums:
            hash[i] = hash.get(i,0)+1
        for i in hash:
            if hash[i] > max_fac:
                max_fac = hash[i]
                max_element = i
        return max_element