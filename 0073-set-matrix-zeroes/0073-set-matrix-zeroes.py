class Solution:   # Optimal solution 
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rowTrack =[0]* n
        colTrack =[0]* m
        for i in range(0,m):
          for j in range(0,n):
            if matrix[i][j] == 0:
             colTrack[i] = -1 
             rowTrack[j] = -1
        
        for i in range(0,m):
          for j in range(0,n):
            if  rowTrack[j] == -1 or colTrack[i] == -1:
              matrix[i][j] = 0
              

