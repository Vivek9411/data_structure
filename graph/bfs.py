
def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
    marked = [0]*V
    ans = []
    q = deque([0])
    marked[0]=1
    while q:
        node = q.popleft()
        ans.append(t)
        for i in adj[t]:
            if not marked[i]:
                marked[i]=1
                q.append(i)
    return ans