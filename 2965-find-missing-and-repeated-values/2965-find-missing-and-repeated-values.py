class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = n*n
        hash = {}
        arr = [0]*2 
        for i in range(0,n):
          for j in range(0,n):
           hash[grid[i][j]] = hash.get(grid[i][j] , 0) +1
        
        for i in range(1,m+1):
            if i in hash:
                if hash[i] == 2:
                  arr[0] = i 
            else:
              arr[1] = i
        return arr