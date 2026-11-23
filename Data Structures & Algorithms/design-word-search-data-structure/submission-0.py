class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_last = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.is_last = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in cur.children:
                        if child and dfs(i+1, child):
                            return True
                    return False
                else:
                    index = ord(char) - ord('a')
                    if not cur.children[index]:
                        return False
                    cur = cur.children[index]
            return cur.is_last
        return dfs(0, self.root)