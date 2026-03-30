class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Two hashmap - Word and Counter
        # Two counters - have and need
        # res, length - var
        # Initiate the counter with t

        word,counterT = {}, {}
        for c in t:
            counterT[c] = 1 + counterT.get(c,0)
        have, need = 0,len(counterT)
        res, subLength = [-1,-1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            word[c] = 1 + word.get(c,0)

            if c in counterT and counterT[c] == word[c]:
                have += 1
            # Valid substring check if it better than what we seen already
            while have == need:
                if (r-l) + 1 < subLength:
                    res = [l,r]
                    subLength = r-l+1
                word[s[l]] -= 1

                if s[l] in counterT and word[s[l]] < counterT[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if subLength < float("infinity") else ""
