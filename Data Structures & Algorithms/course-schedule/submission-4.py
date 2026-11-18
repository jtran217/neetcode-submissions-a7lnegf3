class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapPopulate = {i:[] for i in range(numCourses)}
        visited = set()
        # Populate prereq list.
        for crs,pre in prerequisites:
            mapPopulate[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if mapPopulate[crs] == []:
                return True
            visited.add(crs)

            for pre in mapPopulate[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            mapPopulate[crs] = []
            return True

        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        
