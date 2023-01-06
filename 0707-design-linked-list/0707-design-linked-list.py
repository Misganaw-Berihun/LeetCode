class Node:
    def __init__(self, val = 0, nxt = None):
        self.val = val
        self.next = nxt
        
class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None

    def getNodeAtIndex(self, index: int) -> Node:
        cur = self.head
        i = 0
        
        while i < index and cur:
            cur = cur.next
            i += 1
        
        node = cur
        return node
        
    def get(self, index: int) -> int:
        val = -1
        
        node = self.getNodeAtIndex(index)
        if node:
            val = node.val 
        
        return val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            new_node = Node(val, self.head)
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            new_node = Node(val)
            self.tail.next = new_node
            self.tail = new_node
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.head = Node(val, self.head)
            if not (self.head.next):
                self.tail = self.head
        else:
            node = self.getNodeAtIndex(index - 1)
            if node:
                new_node = Node(val, node.next)
                node.next = new_node
                if not new_node.next:
                    self.tail = new_node
        
    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = self.head
        else:
            node = self.getNodeAtIndex(index - 1)
            if node and node.next:
                node.next = node.next.next
                if node.next == None:
                    self.tail = node
                
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)