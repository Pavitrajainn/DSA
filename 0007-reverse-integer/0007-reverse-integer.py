class Solution:
    def reverse(self, x: int) -> int:
      rev = 0
      if x < 0:
        n = -(x)
      else:
        n = x
      while n > 0:
          r = n % 10
          rev = r + rev * 10
          n = n // 10
      if rev < (-(21**31)) or rev > (2**31 - 1):
        return 0
      if x < 0 : 
         return (-rev)
      else:
        return rev
 
