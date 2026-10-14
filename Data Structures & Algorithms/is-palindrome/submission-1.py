class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(x for x in s if x.isalnum())
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True