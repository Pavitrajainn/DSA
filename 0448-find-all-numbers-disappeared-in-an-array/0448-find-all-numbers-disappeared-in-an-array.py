class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       hash_dis = [0]*(len(nums)+1)
       l =[]
       for i in nums:
        hash_dis[i] += 1
       for j in range(1,len(hash_dis),1) :
         if hash_dis[j] == 0 :
            l.append(j)
       return l    
   