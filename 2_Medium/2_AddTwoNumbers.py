from lib2to3.pytree import Node
from logging import root
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = [[i.val, i.next] for i in l1]
        list2 = [[i.val, i.next] for i in l2]

        iterableList1, iterableList2 = [], []

        iterableList1 = [list1[0][0], list1[0][1], list1[1][1]]
        iterableList2 = [list2[0][0], list2[0][1], list2[1][1]]

        num1 = ''.join([str(i) for i in iterableList1][::-1])
        num2 = ''.join([str(i) for i in iterableList2][::-1])
        return int(num1) + int(num2)

root1 = ListNode(2,4)
node1 = ListNode(4,3)

root2 = ListNode(5,6)
node2 = ListNode(6,4)

list1 = [root1, node1]
list2 = [root2, node2]

answer = Solution()
sol = answer.addTwoNumbers(list1, list2)

print(sol)

class Solu:
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # :type l1: ListNode
    # :type l2: ListNode
    # :rtype: ListNode

        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                        
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
                
        return result.next

answer = Solu()
sol = answer.addTwoNumbers(ListNode([2,4,3]), ListNode([5,6,4]))

print(sol)