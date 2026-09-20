class UnionFind:
    def __init__(self, n: int):
        self.parents=[i for i in range(n)]
        self.size = [1]*n
        self.n_sets = n
    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        y_root = self.find(y)
        x_root = self.find(x)
        if y_root == x_root:
            return False
        for i in range(len(self.parents)):
            if self.parents[i] == y_root:
                self.parents[i] = x_root
        self.n_sets-=1
        return True
    def getNumComponents(self) -> int:
        return self.n_sets

