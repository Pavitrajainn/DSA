class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected  = sorted(heights)
        n = len(heights)
        count = 0
        for i in range(0,n):
         if expected[i] != heights[i]:
            count += 1
        return count