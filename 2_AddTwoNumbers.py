from typing import Optional

list1 = [2,4,3]
list2 =  [5,6,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return l1 + l2



answer = Solution()
answer.addTwoNumbers(list1, list2)

strings = [str(i) for i in list1]
joined = ''.join(strings)
print(joined)

linked = (2)

answer = list1 + list2


print(answer)