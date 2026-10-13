class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp =[]
        for i in range((n-k),n):
            temp.append(nums[i])
        for j in range(n-1,k-1,-1):
            nums[j] = nums[j-k]
        for i in range(0,k):
            nums[i] = temp[i]

        return nums    