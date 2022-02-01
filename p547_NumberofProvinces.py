# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        if size == 0:
            return size
        uf = UnionFind(size)
        for row in range(size):
            for col in range(row+1, size):
                if isConnected[row][col] == 1:
                    uf.union(row,col)
        return uf.getCount()
                
        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
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
            self.count -=1
            
    def connected(self, x,y):
        return self.find(x) == self.find(y)
    
    def getCount(self):
        return self.count