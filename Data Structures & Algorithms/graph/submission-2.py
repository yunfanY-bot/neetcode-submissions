class Graph:
    
    def __init__(self):
        self.adj={}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src]=set()
        self.adj[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj:
            return False
        if dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPathHelper(self, src, dst, visited):
        if src in visited:
            return False
        if src in self.adj:
            if dst in self.adj[src]:
                return True
            visited.add(src)
            for nei in  self.adj[src]:
                if self.hasPathHelper(nei, dst, visited):
                    return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.hasPathHelper(src, dst, visited)


