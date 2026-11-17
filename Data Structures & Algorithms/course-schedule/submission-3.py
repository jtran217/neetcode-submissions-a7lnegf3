class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapCourse = {i:[] for i in range(numCourses)}
        visited = set()
        # Populate prereq
        for crs,pre in prerequisites:
            mapCourse[crs].append(pre)
        

        def dfs(i):
            if i in visited:
                return False
            if mapCourse[i] == []:
                return True
            
            visited.add(i)

            for pre in mapCourse[i]:
                if not dfs(pre):
                    return False
            visited.remove(i)
            mapCourse[i] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True