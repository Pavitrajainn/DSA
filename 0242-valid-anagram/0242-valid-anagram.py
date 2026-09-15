class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        num = True
        for i in s:
          hash_s[i] = hash_s.get(i,0)+1
        for j in t:
          hash_t[j] = hash_t.get(j,0)+1
        for k in s :
           if hash_s.get(k,0) != hash_t.get(k,0):
             num = False
        return num
         
