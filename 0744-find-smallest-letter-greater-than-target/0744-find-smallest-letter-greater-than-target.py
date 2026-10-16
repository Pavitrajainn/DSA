class Solution(object):
    def nextGreatestLetter(self, letters, target):
        n = len (letters)
        for i in letters:
         if i > target :
            return i
        return letters[0]
        
        