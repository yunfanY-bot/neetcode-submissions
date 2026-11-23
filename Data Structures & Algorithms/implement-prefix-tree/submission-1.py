class TreeNode():
    def __init__(self):
        self.childNode = [None] * 26
        self.is_last = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            i  = ord(char) - ord('a')
            if not cur.childNode[i]:
                cur.childNode[i] = TreeNode()
            cur = cur.childNode[i]
        cur.is_last=True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not cur.childNode[i]:
                return False
            cur = cur.childNode[i]
        if not cur.is_last:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            i = ord(char) - ord('a')
            if not cur.childNode[i]:
                return False
            cur = cur.childNode[i]
        return True
        