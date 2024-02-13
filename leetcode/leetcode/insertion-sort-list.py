# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        r = []
        while curr:
            r.append(curr.val)
            curr = curr.next
        return ListNode(",".join(map(str, sorted(r))))



        