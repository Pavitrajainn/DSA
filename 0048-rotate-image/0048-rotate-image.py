class Solution(object):
    def rotate(self, matrix):
      n = len(matrix)
      for i in range(0,n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
      temp = n-1
      for i in range(0,(n/2)):
        for j in range(0,n):
             matrix[j][i],matrix[j][temp-i] = matrix[j][temp-i],matrix[j][i]
