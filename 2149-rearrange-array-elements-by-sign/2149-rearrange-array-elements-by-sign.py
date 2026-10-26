class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr1=[]
        arr2=[]
        arr=[]
        for i in range(0,n):
            if nums[i] < 0 :
               arr2.append(nums[i])
            else:
               arr1.append(nums[i])
        i = j  = 0
        while i < n//2 or j < n//2:
           arr.append(arr1[i])
           i += 1
           arr.append(arr2[j])
           j += 1
        return arr   
