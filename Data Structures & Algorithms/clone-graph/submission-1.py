"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_dict = {}
        
        def dfs(node):
            if node in node_dict:
                return node_dict[node]
            node_dict[node] = Node(node.val)
            for nei in node.neighbors:
                node_dict[node].neighbors.append(dfs(nei))
            return node_dict[node]

        dfs(node)
        return node_dict[node]