import heapq
def dijkstra(self, V, adj, S):
        dist = [-1]*V
        dist[S]=0
        q = [[S,0]]
        while q:
            node,cost = heapq.heappop(q)
            for adj_node, adj_cost in adj[node]:
                i_dist = cost+ adj_cost
                if dist[adj_node]==-1 or i_dist<dist[adj_node]:
                    
                    heapq.heappush(q, [adj_node, i_dist])
                    dist[adj_node]=i_dist
        return dist