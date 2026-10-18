class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        piviot = -1 
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                piviot = i
                break
        if piviot == -1 :
          i = 0
          j = n-1
          while i < j:
             nums[i], nums[j] = nums[j], nums[i]
             i += 1
             j -= 1
          return nums

        else:
          for i in range(n-1,piviot,-1):
            if nums[piviot] < nums[i]:
                nums[piviot],nums[i]= nums[i],nums[piviot]
                break
          i = piviot + 1 
          j = n-1 
          while i<j:
            nums[i],nums[j]= nums[j],nums[i]
            i+=1
            j-=1
          return nums

