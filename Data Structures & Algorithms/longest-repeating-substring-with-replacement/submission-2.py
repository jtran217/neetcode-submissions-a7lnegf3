class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window 
        # What condition do we adjust our window on? -> If num of replacable > k we shift left pointer
        # k replacement avaliable -> length of current s - highest count  (AAAY) 4 - 3 = 1, so one k used

        m_length = 0
        charSet = set(s)
        for c in charSet:
            count = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r-l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                m_length = max(m_length,(r-l)+1 )
        return m_length
                    