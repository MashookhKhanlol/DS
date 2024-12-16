from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        last = len(s)-1
        first = 0

        while last > first:
            s[first] , s[last] = s[last] , s[first]
            first+=1
            last-=1
        
        return s
    
solurion = Solution()

test = solurion.reverseString(["h","w","w","g"])

print(test)
