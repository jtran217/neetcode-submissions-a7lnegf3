class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagram = {}

        for s in strs:
            sortS = "".join(sorted(s))
            if sortS not in groupedAnagram:
                groupedAnagram[sortS] = []
            groupedAnagram[sortS].append(s)
        return list(groupedAnagram.values())
