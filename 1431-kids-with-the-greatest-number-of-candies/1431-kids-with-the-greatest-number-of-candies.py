class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
     l=[True if i + extraCandies >= max(candies) else False for i in candies]
     return l