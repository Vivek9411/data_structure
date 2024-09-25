class Trie:
    def __init__ (self):
        self.index = {}
        self.count = 0
    
    def insert(self, root,w):
        temp = root
        for i in w:
            if i not in temp.index.keys():
                temp.index[i]= Trie()
            temp = temp.index[i]
            temp.count+=1 
    
    def search(self,root,w):
        temp = root
        ans = 0
        for i in w:
            if i not in temp.index.keys():
                return ans
            temp = temp.index[i]
            ans+= temp.count
        return ans