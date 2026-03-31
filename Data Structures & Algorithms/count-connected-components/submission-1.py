class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build Adjacency graph
        # Traverse dfs each node ->  may be disconnected pieces
        # When done exploring one node return True and increment some counter

        graph = {}
        for i in range(n):
            graph[i] = []
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(graph,node,visited):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(graph,neighbor,visited)
            return True

        count = 0
        for node in graph:
            if dfs(graph,node,visited):
                count += 1
        
        return count
