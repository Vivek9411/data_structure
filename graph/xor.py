class Node:
    def __init__(self):
        self.array = [None]*2
    def contain_keys(self, key):
        if self.array[key]:
            return True
        
        return False
    def get(self, key):
        return self.array[key]
    
    def put(self, key,node):
        self.array[key]=node

class trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, n):
        node= self.root
        for i in range(31, -1, -1):
            temp = n&(1<<i)
            if temp:
                if not node.contain_keys(1):
                    node.put(1,Node())
                node = node.get(1)
            else:
                if not node.contain_keys(0):
                    node.put(0, Node())
                node= node.get(0)
    def find(self,n):
        node=self.root
        if node.get(0) ==None and node.get(1)==None:
            return -1
        ans = 0
        for i in range(31,-1,-1):
            temp = n&(1<<i)
            if temp:
                if node.contain_keys(0):
                    ans = ans|(1<<i)
                    node = node.get(0)
                else:
                    node=node.get(1)
            else:
                if node.contain_keys(1):
                    ans = ans|(1<<i)
                    node = node.get(1)
                else:
                    node=node.get(0)
        return ans