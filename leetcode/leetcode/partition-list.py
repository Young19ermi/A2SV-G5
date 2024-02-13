
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        l = less = ListNode(0)
        g = greater = ListNode()
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = ListNode(curr.val)
                less = less.next # we need to shift
            else:
                greater.next = ListNode(curr.val)
                greater = greater.next
            curr = curr.next

        less.next = g.next
        
        return l.next


        # l = []
        # curr = head
        # if not head:
        #     return None
        # elif not(head.next):
        #     return head
        # while curr:
        #     if curr.val < x:
        #         l.append(curr.val)
        #     curr = curr.next
        # N = ListNode(",".join(map(str, l)))

        # r = []
        # curr = head

        # while curr:
        #     if curr.val >= x:
        #         r.append(curr.val)
        #     curr = curr.next
            
        # N = ListNode(",".join(map(str, l)))
        # K = ListNode(",".join(map(str, r)))
        # N.next = K.next
        # print(N)
        # return N






    







        # nums = []
        # curr = head
        # while curr:
        #     nums.append(curr.val)
        #     curr = curr.next
        # ans = []
        
        # for n in range(len(nums)):
        #     if nums[n] < x:
        #         ans.append(",".join(int(map(str, nums[n]) * 3)))
                
        #         print(n)
        # # print(ans)
        # # print(nums)
        # for n in nums:
        #     ans.append(n)
        
        # return ListNode(",".join(map(str, ans)))


        