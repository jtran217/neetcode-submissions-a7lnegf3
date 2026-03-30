class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_hash = {}
        flag = False
        for s in strs:
            # Init case when hash empty
            if not result_hash:
                result_hash[s] = []
                continue
            s_sorted = "".join(sorted(s))
            for key,value in result_hash.items():
                key_sorted = "".join(sorted(key))
                if s_sorted == key_sorted:
                    result_hash[key].append(s)
                    flag = True
                    break
            if not flag:
                result_hash[s] = []
            flag = False
        print(result_hash)
        final_result = [[key] + value for key, value in result_hash.items()]
        return final_result
       
        