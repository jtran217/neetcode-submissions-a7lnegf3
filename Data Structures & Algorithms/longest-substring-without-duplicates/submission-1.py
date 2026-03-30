class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window pattern -> Two pointers, Hash set to track what we seen
        # Know when we extend the window:
        # If s[r] in hashset remove s[l] and increment it -> This is our condition


        seen = set()
        l = 0
        mLength = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            mLength = max(mLength, r-l + 1)
            seen.add(s[r])
        return mLength