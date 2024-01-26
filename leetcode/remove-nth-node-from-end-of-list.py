# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        x = dummy 
        y = dummy
        for _ in range(n):
            y = y.next
        while y.next:
            x = x.next
            y = y.next
        x.next = x.next.next
        return dummy.next


        