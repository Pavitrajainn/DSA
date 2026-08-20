class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        hash_ar  =[]
        for i in range(0,len(accounts)):
          max_sum = 0
          for j in range(0,len(accounts[i])):
            max_sum = max_sum + accounts[i][j]
          hash_ar.append(max_sum)
        return max(hash_ar)
              