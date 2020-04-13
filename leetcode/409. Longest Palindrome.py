class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for i in s:
            counter[i] = counter.get(i, 0) + 1
        pairs = 0
        single = False
        for key in counter:
            pairs += counter[key]// 2
            if not single and counter[key] % 2 == 1:
                single = True
        if single:
            return 2* pairs + 1
        else:
            return 2 * pairs
                
            
            
