# V is number of vertices 
# adj is adjacecncy list 

from heapq import heappop, heappush

def spanningTree(V, adj):
    vis = [0]*(V+1) 
    # print(adj)
    mst = []
    
    q = [[0, 0, -1]]
    cost = 0
    while q:
        weight, start, parent= heappop(q)
        if vis[start]==0:
            vis[start]=1
            if parent !=-1:
                mst.append([parent, start, weight])
                # print(parent)
                # print([start])
                # print([weight])
            cost += weight 
            
            for i in adj[start]:
                # print(i)
                if vis[i[0]]==0:
                    heappush(q, [i[1], i[0], start])
    
    print(mst)
    return cost
                