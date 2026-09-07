class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index):
            if cur is None:
                return -1
            cur = cur.next
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        if self.head==None:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next != None:
            cur=cur.next
        new_tail= Node(val)
        new_tail.val = val
        cur.next = new_tail

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        cur = self.head
        pre = cur
        for i in range(index):
            pre=cur
            if cur == None:
                return False
            cur = cur.next
        if cur == None:
            return False
        pre.next = cur.next
        return True
        

    def getValues(self) -> List[int]:
        to_return = []
        cur=self.head
        while cur != None:
            to_return.append(cur.val)
            cur= cur.next
        return to_return
