class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = ''
        max_length = 0
        for i in s:
            if i not in substr:
                substr += i
            else:
                max_length = max(max_length, len(substr))
                substr = substr[substr.index(i) + 1:] + i
        max_length = max(max_length, len(substr))
        return max_length
