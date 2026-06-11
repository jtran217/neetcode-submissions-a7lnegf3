class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            collection[key].append(s)
        result = list(collection.values())
        return result
