class Node:
    def __init__(self, value):
        self.value = value
        self.prev=None
        self.next=None
class Deque:
    
    def __init__(self):
        self.head = None

    def isEmpty(self) -> bool:
        return self.head is None
        
    def append(self, value: int) -> None:
        if self.isEmpty(): 
            self.head = Node(value)
            return
        cur=self.head
        while cur.next !=None:
            cur=cur.next
        cur.next=Node(value)
        cur.next.prev=cur
        
    def appendleft(self, value: int) -> None:
        new_head = Node(value)
        if not self.isEmpty():
            new_head.next = self.head
            self.head.prev = new_head
        self.head = new_head
        
    def pop(self) -> int:
        if self.isEmpty(): 
            return -1
        cur=self.head
        while cur.next !=None:
            cur=cur.next
        pre = cur.prev
        if pre == None:
            self.head = None
        else:
            pre.next = None
        return cur.value
        
    def popleft(self) -> int:
        if self.isEmpty(): 
            return -1
        res = self.head.value
        next = self.head.next
        if next != None:
            next.prev = None
        self.head = next
        return res
            
        
