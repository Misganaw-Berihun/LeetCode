#User function Template for python3

'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

'''
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
'''

def reorderList(self):
        slow = head
        fast = head
        cur = head
        stack = []
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        cur = slow
        while cur:
            stack.append(cur)
            cur = cur.next
            
        cur = head
        while cur != slow and stack:
            temp = cur.next
            top = stack.pop()
            cur.next = top
            top.next = temp
            cur = temp
            
        cur.next = None
        return head
    # write code to reorder Nodes of Linked_List

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    reorder_List = reorderList

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reorder_List()
        lis.printList()

# } Driver Code Ends