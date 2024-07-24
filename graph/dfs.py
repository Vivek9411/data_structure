def dfsOfGraph(self, V, adj):
    visited =[0]*V
    start=0
    ans  = []
    
    def dfs(start, adj,visited, ans):
        visited[start]=1
        ans.append(start)
        for  i in adj[start]:
            if not visited[i]:
                dfs(i, adj, visited, ans)
    
    dfs(start, adj, visited, ans)
    return ans