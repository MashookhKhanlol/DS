from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        p1, p2 = 0, 0

        # Merge the two arrays
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
            else:
                ans.append(nums2[p2])
                p2 += 1
        
        # Append remaining elements
        if p1 < len(nums1):
            ans.extend(nums1[p1:])
        if p2 < len(nums2):
            ans.extend(nums2[p2:])
        
        # Calculate the median
        length = len(ans)
        if length % 2 == 1:  # Odd length
            return ans[length // 2]
        else:  # Even length
            mid = length // 2
            return (ans[mid - 1] + ans[mid]) / 2.0