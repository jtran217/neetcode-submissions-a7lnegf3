class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqCount = {}
        
        for c in s:
            if c not in freqCount:
                freqCount[c] = 0
            freqCount[c] += 1

        for c in t:
            if c not in freqCount:
                return False
            freqCount[c] -= 1
            if freqCount[c] < 0:
                return False
        
        for c in freqCount:
            if freqCount[c] != 0:
                return False
        return True
