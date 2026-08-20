class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        hash_ar =[]
        for i in range(0,n):
            hash_ar.append(nums[i])
            hash_ar.append(nums[n+i])
        return hash_ar
