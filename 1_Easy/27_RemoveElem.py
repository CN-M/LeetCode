from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]

answer = Solution()
result = answer.removeElement(nums, 1)
print(result)