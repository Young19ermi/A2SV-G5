from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        q = deque()
        for i in range(len(deck)):
            q.appendleft(deck[i])
            l = q.pop()
            q.appendleft(l)
        last = q.popleft()
        q.append(last)
        return q



        # deck.sort()
        # k  = len(deck)//2
        # left = []
        # right = []
        # maximum = max(deck)
        # for i in range(k+1):
        #     left.append(deck[i])
        
        # for n in range(k,len(deck)-1):
        #     right.append(deck[n])

        # res = []
        # for n in left:
        #     res.append(n)
        # res.append(maximum)

        # for n in right:
        #     res.append(n)
        # return res

        # q = deque()
        # for n in res:
        #     q.append(n)
        return

        

        


        

















        # return []
        # # left = []
        # # right= []
        # # deck.sort()
        # # for n in range((len(deck)//2) + 1):
        # #     left.append(deck[n])
        # # k = len(deck)//2
        # # for n in range(n+1, len(deck)):
        # #     right.append(deck[n])
        # # right.sort(reverse =True)
        # # for n in right:
        # #     left.append(n)

        # # q = deque()
        # # for n in left:
        # #     q.append(n)
        # # res = []
        # # while q:
        # #     l = q.popleft()
        # #     r = q.pop()
        # #     res.append(l)
        # #     res.append(r)
        # # return res