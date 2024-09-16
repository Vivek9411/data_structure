
class Node:
    def __init__(self):
        self.link = [None]*26
        self.count = 0
        self.end = 0
    
    def contain_keys(self, ch):
        return  self.link[ord(ch)-ord('a')] is not None 
    
    def get(self, ch):
        return self.link[ord(ch)-ord('a')]
    
    def put(self,ch, node):
        self.link[ord(ch)-ord('a')]=node  
    
    def set_end(self,x):
        self.end+=x 

    def set_count(self,x):
        self.count+= x
    
    def get_end(self):
        return self.end
    
    def get_count(self):
        return self.count
    


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root 
        for ch in word:
            if not node.contain_keys(ch):
                node.put(ch, Node())
            new_node= node.get(ch)
            new_node.set_count(1)
            node = new_node
        node.set_end(1)

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if not node.contain_keys(ch):
                return 0 
            new_node = node.get(ch)
            node= new_node
        return node.get_end()

    def countWordsStartingWith(self, word):
        node = self.root
        for ch in word:
            if not node.contain_keys(ch):
                return 0 
            
            new_node = node.get(ch)
            node = new_node

        return node.get_count()

    def erase(self, word):
        node = self.root
        for ch in word:
            new_node = node.get(ch)
            if new_node.get_count()==1:
                node.put(ch, None)
            new_node.set_count(-1)
            node = new_node
        
        node.set_end(-1)
