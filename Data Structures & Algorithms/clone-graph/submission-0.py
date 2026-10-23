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
        node_dict[node] = Node(node.val)
        q = deque([node])
        while q:
            cur_node = q.popleft()
            for nei in cur_node.neighbors:
                if nei not in node_dict:
                    node_dict[nei] = Node(nei.val)
                    q.append(nei)
                node_dict[cur_node].neighbors.append(node_dict[nei])
                

        return node_dict[node]