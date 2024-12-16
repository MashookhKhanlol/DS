class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        test1 = {}
        test2 = {}

        for char in s:
            test1[char] = test1.get(char,0)+1
        
        for char in t:
            test2[char] = test2.get(char,0)+1

        return test1==test2 
        