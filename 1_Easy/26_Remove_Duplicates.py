from operator import indexOf
from turtle import numinput
from typing import List

from attr import has


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash = []
        for i, n in enumerate(nums):
            if n in hash:
                nums.remove(n)
            else:
                hash.append(n)
        nums.clear()
        nums = hash

        return nums

nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]

answer = Solution()

print(answer.removeDuplicates(nums))
