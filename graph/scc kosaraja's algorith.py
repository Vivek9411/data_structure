# three step algortihm  to find scc(stronlgy connected components) Kosaraju's Algorithm
# 1-> Sort all the nodes according to their finishing time:
# 2:-> Reverse all the edges of the entire graph:
# 3:-> Perform the DFS and count the no. of different DFS calls to get the no. of SCC:


def kosaraju(self, V, adj):
    vis = [0]*V
    stack =[]

    # step 1
    # for sorting node according to there functional time and storing them in stack
    def dfs(node, adj, vis, stack):
        vis[node]=1
        for i in adj[node]:
            if vis[i]==0:
                dfs(i, adj, vis, stack)
        
        stack.append(node)
    for i in range(V):
        if vis[i]==0:
            dfs(i, adj, vis, stack)
    
    # completion of step one 
    


    
    # step 2
    # reverse the order of edges 
    # if a edge starts from a->b in adj then is becomes b->a in adjt
    adjt = [[] for i in range(V)]
    for i in range(V):
        for j in adj[i]:
            adjt[j].append(i)
    
    # completion of step 2 


    # step 3 Perform the DFS and count the no. of different DFS calls to get the no. of SCC
    vis = [0]*V
    def dfs3(node, adjt, vis):
        vis[node]=1
        for i in adjt[node]:
            if vis[i]==0:
                dfs3(i, adjt, vis)
    
    count=0
    
    # perform dfs in order of functional time of graph
    while stack:
        i = stack.pop()
        if vis[i]==0:
            count+=1 
            dfs3(i, adjt, vis)
    
    return count
    