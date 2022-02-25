class Node:
    def __init__(self,data = 0,next = None):
        self.val = data
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        i = 0
        cur = self.head
        
        while i < index :
            cur = cur.next
            i += 1
            
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        if self.head:
            newNode = Node(val,self.head)
        else:
            newNode = Node(val)
        
        self.head = newNode
        self.size += 1
            
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
                
            cur.next = newNode
        else:
            self.head = newNode
            
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        
        i = 0    
        cur = self.head
        while i < index - 1:
            cur = cur.next
            i += 1
            
        newNode = Node(val,cur.next)
        cur.next = newNode   
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            i = 0
            cur = self.head
            
            while i < index - 1:
                cur = cur.next
                i += 1
                
            cur.next = cur.next.next
        
        self.size -= 1
                

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)