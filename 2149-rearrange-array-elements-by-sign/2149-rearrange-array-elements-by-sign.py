class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr1=[]
        arr2=[]
        for i in range(0,n):
            if nums[i] < 0 :
               arr2.append(nums[i])
            else:
               arr1.append(nums[i])

        for i in range(0,n//2):
           nums[2*i]=arr1[i]
           nums[(2*i)+1]=arr2[i]
        return nums
