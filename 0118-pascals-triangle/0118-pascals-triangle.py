class Solution(object):
    def generate(self, numRows):
        arr =[]
        def factorial(n):
           fact = 1  
           for i in range(n,0,-1):
             fact *= i
           return fact
        def combination(i , j):
            return factorial(i)//(factorial(j) * factorial(i-j))
        
        for i in range(0,numRows):
            arg =[]
            for j in range(0,i+1):
              arg.append(combination(i,j))
            arr.append(arg)
        return arr