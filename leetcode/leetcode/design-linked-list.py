class Node:
    def __init__(self , value = 0):
        self.data = value
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0
        
    def get(self, index: int) -> int:
        if index < self.len:
            temp = self.head
            for _ in range(index):
                temp = temp.next
                if not temp:
                    return -1

            return temp.data
        
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.len += 1
        
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head

            while temp.next:
                temp = temp.next
            temp.next = newNode
        self.len += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.len:
            if index == 0:
                self.addAtHead(val)
            else:
                temp = self.head
                newNode = Node(val)

                for _ in range(index-1):
                    temp = temp.next
          
                newNode.next = temp.next
                temp.next = newNode
            self.len += 1
    def deleteAtIndex(self, index: int) -> None:
        if self.head and index < self.len:
            if index == 0:
                self.head = self.head.next
            else:
                temp = self.head
            
                for _ in range(index-1):
                    temp = temp.next
        
                temp.next = temp.next.next
                  
            self.len -= 1
       