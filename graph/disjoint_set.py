class Disjointset:
    __n:None
    __parent:None
    __rank:None
    __height:None

    def __init__(self, n:int):
        self.__n = n 
        self.__parent = [i for i in range(n+1)]
        self.__rank = [0]*(n+1)
        self.__height = [1]*(n+1)

    def ult_parent(self, i)->int:
        if self.__parent[i]==i:
            # print(self.__parent)
            return i  

        self.__parent[i] = self.ult_parent(self.__parent[i])
        return self.__parent[i]

    def Union_By_rank(self, node1:int, node2:int)->None:
        Up_node1 = self.ult_parent(node1)
        Up_node2 = self.ult_parent(node2)

        if Up_node1==Up_node2:
            return  

        if self.__rank[Up_node1]>self.__rank[Up_node2]:
            self.__parent[Up_node2]=Up_node1 
        elif self.__rank[Up_node1]<self.__rank[Up_node2]:
            self.__parent[Up_node1]=Up_node2
        else:
            self.__parent[Up_node2]=Up_node1
            self.__rank[Up_node1]+=1 

    def Union_By_Height(self, node1:int, node2:int)->None:
        Up_node1 = self.ult_parent(node1)
        Up_node2 = self.ult_parent(node2)

        if Up_node1==Up_node2:
            return 

        if self.__height[Up_node1]>self.__height[Up_node2]:
            self.__parent[Up_node2]=Up_node1
            self.__height[Up_node1]+= self.__height[Up_node2]
        else:
            self.__parent[Up_node1]=Up_node2
            self.__height[Up_node2]+= self.__height[Up_node1]

    def getter(self):
    	print(self.__parent)

    def get_height(self, n=None):
    	if n:
    		print(self.__height[self.ult_parent(n)])
    	else:
    		print(self.__height)
    def get_rank(self, n=None):
    	if n:
    		print(self.__rank[self.ult_parent(n)])
    	else:
    		print(self.__rank)




# # how to use class using union by rank
# d = Disjointset(7)
# d.Union_By_rank(1,2)
# d.Union_By_rank(2,3)
# d.Union_By_rank(4,5)
# d.Union_By_rank(6,7)
# d.Union_By_rank(5,6)

# if d.ult_parent(3)==d.ult_parent(7):
#     print(True)
# else:
#     print(False)
# d.Union_By_rank(3,7)
# if d.ult_parent(3)==d.ult_parent(7):
#     print(True)
# else:
#     print(False)
# # print(d.ult_parent(2))
# # print(d.ult_parent(3))


# how to use disjoint set using union by height
d = Disjointset(7)
d.Union_By_Height(1,2)
d.Union_By_Height(2,3)
d.Union_By_Height(4,5)
d.Union_By_Height(6,7)
d.Union_By_Height(5,6)

if d.ult_parent(3)==d.ult_parent(7):
    print(True)
else:
    print(False)
d.Union_By_Height(3,7)
if d.ult_parent(3)==d.ult_parent(7):
    print(True)
else:
    print(False)
d.get_height()
d.get_height(1)
print(d.getter())

# print(d.ult_parent(2))
# print(d.ult_parent(1))
# print(d.ult_parent(3))

