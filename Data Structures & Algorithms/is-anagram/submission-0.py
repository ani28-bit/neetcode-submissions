class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freqs = [0] * 26
        freqt = [0] * 26

        for i in range(0, len(s)):
            freqs[ord(s[i]) - ord('a')] += 1
            freqt[ord(t[i]) - ord('a')] += 1

        for i in range(0, 26):
            if freqs[i] != freqt[i]:
                return False

        return True