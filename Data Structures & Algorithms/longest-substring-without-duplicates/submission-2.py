class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        # Change left pointer when s[r] is something already seen
        l = 0
        count = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                continue
            count = max(count, r-l+1)
            seen.add(s[r])
            
        return count