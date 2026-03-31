class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key = sorted string
        dic = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            dic[key].append(s)
        res = []
        for value in dic.values():
            res.append(value)

        return res 


