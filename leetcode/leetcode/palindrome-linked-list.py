# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #Get the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse it
        dummy = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = dummy
            dummy = curr
            curr = temp
        
        #Checking part
        left = head # the head have been modified 
        right = dummy
         
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True
        