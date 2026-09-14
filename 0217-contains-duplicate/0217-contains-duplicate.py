class Solution(object):
    def containsDuplicate(self, nums):
     n = False
     hash_dict = {}
     for i in nums:
        hash_dict[i] = hash_dict.get(i,0)+1
     for j in hash_dict:
        if hash_dict[j] >= 2:
            n = True
     return n
        