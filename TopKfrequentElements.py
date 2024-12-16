

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        sorted_nums = sorted(dic.keys(), key= lambda x:dic[x],reverse=True)
        return sorted_nums[:k]
