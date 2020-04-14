class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) <= 1:
            return ''
        for ind, i in enumerate(palindrome):
            if i !='a':
                if ind == len(palindrome)//2 and len(palindrome) % 2 == 1:
                    return palindrome[:-1] + 'b'
                return palindrome[:ind] + 'a' + palindrome[ind + 1:]
            
        return palindrome[:-1] + 'b'
