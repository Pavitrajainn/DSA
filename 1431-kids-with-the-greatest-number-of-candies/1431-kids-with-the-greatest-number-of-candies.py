class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      l =[]
      maxcandies = 0
      for i in candies:
        i+= extraCandies
        maxcandies = max(candies)
        if i >= maxcandies:
            l.append(True)
        else:
            l.append(False)
      return l