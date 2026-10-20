class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        def setInfinite(matrix,row,col):
            for i in range(0,m):
                 if matrix[i][col] != 0:
                    matrix[i][col] = float("inf") 
            for j in range(0,n):
                 if matrix[row][j] != 0:
                    matrix[row][j] = float("inf") 
                    
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    setInfinite(matrix,i,j)


        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
                