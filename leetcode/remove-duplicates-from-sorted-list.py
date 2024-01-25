# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = head
        if not head:
            return None
        else:
            print(head)
            print(head.next)
            while head.next:
                if head.val == head.next.val:
                    head.next = head.next.next
                else:
                    head = head.next
            return dummy
