# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        x = dummy
        y = dummy
        for _ in range(n):
            y = y.next
        while y and y.next:
            x = x.next
            y = y.next
        x.next = x.next.next
        return dummy.next