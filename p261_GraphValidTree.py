# 261. Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return n==1
        uf = UnionFind(n)

        for row in range(len(edges)):
            uf.union(edges[row][0],edges[row][1])

        return n-1 == uf.getCountEdges() and uf.getCount() ==1
        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size
        self.edge_count = 0
    
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1
            self.count-=1
        self.edge_count+=1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def getCount(self):
        return self.count
    
    def getCountEdges(self):
        return self.edge_count