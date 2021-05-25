<<<<<<< HEAD
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        while head:
            temp_head = head
            head = head.next
            temp_head.next = previous
            previous = temp_head
        return previous
=======
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        while head:
            temp_head = head
            head = head.next
            temp_head.next = previous
            previous = temp_head
        return previous
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
