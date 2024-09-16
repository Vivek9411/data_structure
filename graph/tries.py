class Node:
    def __init__(self):
        self.link = [None]*26
        self.flag =False

    def contain_keys(self, ch):
        return self.link[ord('a')-ord(ch)] is not None
    
    def put(self, ch , node):
        self.link[ord('a')-ord(ch)]=node
    
    def get(self, ch):
        return self.link[ord('a')-ord(ch)]

    def set_end(self):
        self.flag = True
    
    def get_end(self):
        return self.flag
    

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contain_keys(ch):
                node.put(ch,Node())
            new_node = node.get(ch)
            node =new_node
        node.set_end()

    def search(self, word: str) -> bool:
        node = self.root
        for ch in  word:
            if not node.contain_keys(ch):
                return False
            new_node = node.get(ch)
            node = new_node
        
        if node.get_end():
            return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.contain_keys(ch):
                return False
            
            new_node = node.get(ch)
            node =new_node
        
        return True
        