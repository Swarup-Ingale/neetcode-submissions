class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        a = {}
        for i in s:
            a[i] = a.get(i, 0) + 1
        
        for j in t:
            if j not in a or a[j] == 0:
                return False
            a[j] -= 1
        return True
        
        