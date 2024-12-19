from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum_map = {}  # Stores the first occurrence of a prefix sum
        current_sum = 0
        max_length = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            # Check if the entire array up to index i has a sum equal to k
            if current_sum == k:
                max_length = i + 1

            # Check if there exists a subarray with sum k
            if current_sum - k in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[current_sum - k])

            # Store the current sum if it's not already in the hashmap
            if current_sum not in prefix_sum_map:
                prefix_sum_map[current_sum] = i

        return max_length