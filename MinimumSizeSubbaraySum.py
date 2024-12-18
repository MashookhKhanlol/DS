class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        
        total = 0

        ans = float('inf')
        for p2 in range(len(nums)):
            total += nums[p2]
            while total >= target:
                ans = min(ans ,p2-p1+1)
                total -= nums[p1]
                p1+=1

        return ans if ans != float('inf') else 0