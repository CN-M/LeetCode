from typing import List

# targ = 9
# numbers = [2,7,11,15]

# targ = 4
# numbers = [2,1,5,3]

targ = 6
numbers = [3,3]

class Solution:
    def twoSumV1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    answer = nums[i] + nums[j]
                    if answer == target:
                        return [i, j]
                else:
                    pass
    
    def twoSumV2(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value : index
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[n] = i


sums = Solution()
answer = sums.twoSumV2(numbers, targ)

print(answer)






































