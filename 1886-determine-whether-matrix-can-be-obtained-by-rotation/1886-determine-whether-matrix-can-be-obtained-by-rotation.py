class Solution(object):
    def findRotation(self, mat, target):
      n = len(mat)
      for i in range(0,4):
        for i in range(0,n):
          for j in range(i+1,n):
              mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
  
        for i in range(0,(n/2)):
          for j in range(0,n):
               mat[j][i],mat[j][(n-1)-i] = mat[j][(n-1)-i],mat[j][i]  
        
        if mat == target:
            return True

      return False