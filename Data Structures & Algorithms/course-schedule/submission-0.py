class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Generate a directed graph based on prerequisites.
        # From there do a traversal and at any point if we hit a cycle -> Return False

        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a,b in prerequisites:
            graph[a].append(b)
        visited = set()

        def findCyclic(graph,node,visiting):
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            for neighbor in graph[node]:
                if findCyclic(graph,neighbor,visiting):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        for node in graph:
            if findCyclic(graph,node,set()):
                return False
        
        return True
        