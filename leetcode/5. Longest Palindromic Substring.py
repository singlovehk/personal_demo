class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxword = ''
        maxlen = 0
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if maxlen>= j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    maxlen = j - i
                    maxword = s[i:j]
                    break
        return maxword
