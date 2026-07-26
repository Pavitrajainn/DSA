class Solution:
    def countDigits(self, num: int) -> int:
        count = val = 0
        temp = num 
        while num > 0 :
            val = num % 10
            if temp % val == 0 :
                count += 1
            num //= 10
        return count

        