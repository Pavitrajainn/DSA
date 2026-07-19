class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = rev_num = 0
        forward = x
        while x > 0 :
            r = x % 10
            rev_num = r + rev_num * 10
            x = x // 10
        if forward == rev_num :
            return True
        else :
            return False
    
       