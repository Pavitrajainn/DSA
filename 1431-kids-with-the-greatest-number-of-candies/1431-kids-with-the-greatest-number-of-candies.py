class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      l =[]
      maxcandies = max(candies)
      for i in candies:
        i+= extraCandies
        if i >= maxcandies:
            l.append(True)
        else:
            l.append(False)
      return l
    l=[]