from cmath import inf
from typing import List

class Solution:
    def BestTime(self, nums : List[int]) -> List[int]:
        maxPrice = 0
        minPrice = float(inf)

        for num in nums:
            minPrice = min(num , minPrice)

            profit = num - minPrice

            maxPrice = max(profit , maxPrice)

        
        return maxPrice


solution = Solution()

result = solution.BestTime([1,2,4,9,3,90])

print(result)