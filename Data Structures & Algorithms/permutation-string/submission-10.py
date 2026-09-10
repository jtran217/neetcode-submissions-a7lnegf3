class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            if s1Freq[i] == s2Freq[i]:
                match += 1
        l = 0
        for r in range(len(s1),len(s2)):
            if match == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Freq[index] += 1
            if s1Freq[index] == s2Freq[index]:
                match += 1
            elif s1Freq[index] + 1 == s2Freq[index]:
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Freq[index] -= 1
            if s1Freq[index] == s2Freq[index]:
                match += 1
            elif s1Freq[index] -1 == s2Freq[index]:
                match -=1
            l+=1
        return match == 26

            
