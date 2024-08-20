class Disjointset:
    __n:None
    __parent:None
    __rank:None
    __height:None

    def __init__(self, n:int):
        self.__n = n 
        self.__parent = [i for i in range(n+1)]
        self.__rank = [0]*(n+1)
        self.__height = [0]*(n+1)

    def ult_parent(self, i)->int:
        if self.__parent[i]==i:
            print(self.__parent)
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
            self.__height[Up_node1]+= self.__height[Up_node1]
        else:
            self.__parent[Up_node1]=Up_node2
            self.__height[Up_node2]+= self.__height[Up_node1]


# V is number of vertices
# adj is adj list in form of [[[1,5],[2,3]]] means 0->1 with weight of 5, 0-> with weight of 3

def spanningTree(self, V, adj):
    edges = []
    # emplty list with will contain edges in form of [[weight, start, end ]]
    for i in range(V):
        for node, weight in adj[i]:
            edges.append([weight, i, node])
    edges.sort()
    # final list of edges after looping through adj
    # creating an object d form class disjointet for v vertices 

    d = Disjointset(V)
    ans  =0
    mst = []
    for w, s, e in edges:
        # adding new edges with minimum weight if there does not have same ultimate parent (meaning s and e are disjoint till now)
        if d.ult_parent(s)!= d.ult_parent(e):
            d.Union_By_Height(s, e)
            mst.append([s, e, w])
            # add edge to mst
            ans+=w 
    
    return ans
                