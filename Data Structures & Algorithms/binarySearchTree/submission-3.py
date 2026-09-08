class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None  

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        if self.root == None:
            self.root = newNode
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left == None:
                    cur.left = newNode
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right == None:
                    cur.right = newNode
                    return
                cur = cur.right
            else:
                cur.val = val
                return
        
            

    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1


    def getMin(self) -> int:
        cur = self.root
        if cur == None:
            return -1
        while cur.left != None:
            cur = cur.left
        return cur.val


    def getMax(self) -> int:
        cur = self.root
        if cur == None:
            return -1
        while cur.right != None:
            cur = cur.right
        return cur.val

    def findMin(self, node: Node) -> Node:
        while node.left != None:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: Node, key: int) -> Node:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr
        

    def getInorderKeys(self) -> List[int]:
        return self.traverse_helper(self.root)

    def traverse_helper(self, node):
        if node == None:
            return []
        else:
            return self.traverse_helper(node.left) + [node.key] + self.traverse_helper(node.right)
