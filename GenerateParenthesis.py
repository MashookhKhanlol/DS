from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(current_string,opencount,closecount):
            if len(current_string)==n*2:
                result.append(current_string)
                return
            
            if opencount < n:
                generate(current_string+'(',opencount+1,closecount)
            
            if closecount < opencount:
                generate(current_string+')',opencount,closecount+1)

        result = []
        generate("",0,0)
        return result