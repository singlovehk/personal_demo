class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def reverse(i):
            ans = 0
            while i :
                ans = ans*10 + i % 10
                i = i // 10
            return ans
        if x < 0:
            return False
        else :
            return reverse(x) == x
            
## Using String:

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
