class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqueChar = set(s)
        maxLength = 0
        for c in uniqueChar:
            # size 4, we are replacing with x, E 1 2x, 2y, n = 4. size 4 - 2 y = 2x to replace == k so
            # can replace.
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r-l+1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l+=1
                maxLength = max(maxLength,r-l+1)
        return maxLength
                    
                
                