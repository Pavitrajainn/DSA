class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
     maxcandies = max(candies)
     l=[True if i + extraCandies >= maxcandies else False for i in candies]
     return l