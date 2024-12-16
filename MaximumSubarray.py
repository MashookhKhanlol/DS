from typing import List

class Solution:
    def MaxSubarray(self, nums: List[int])->List[int]:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            curr_sum = max(curr_sum+nums[i], nums[i])
            max_sum = max(max_sum,curr_sum)

        return max_sum
    
solution = Solution()

result = solution.MaxSubarray([1,21,4,1,4,42,-2,4])

print(result)