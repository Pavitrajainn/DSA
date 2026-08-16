class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_dup = {}
        for i in nums:
            hash_dup[i] = hash_dup.get(i,0)+1
        for x in hash_dup.values():
            if x >= 2:
                return True 
        else:
             return False