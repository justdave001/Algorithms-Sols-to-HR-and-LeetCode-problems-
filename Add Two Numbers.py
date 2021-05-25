# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        test = ListNode(0)
        residual = test
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                addition1 = l1.val
                l1 = l1.next
            elif not l1:
                addition1 = 0
            if l2:
                addition2 = l2.val
                l2 = l2.next
            elif not l2:
                addition2 = 0
            quotient, remainder = divmod(addition1+addition2+carry, 10)
            carry = quotient
            test.next = ListNode(remainder)
            test = test.next
        return residual.next
            
