class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x >= 2**31 - 1 or x <= -2 ** 31:
            return 0
        
        if x < 0:
            ans = -int(str(x)[-1:0:-1])
        else:
            ans = int(str(x)[::-1])
        if ans >= 2**31 - 1 or ans <= -2 ** 31:
            return 0
        return ans
        
## Using Recursion
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def helper(i):
            ans = 0
            while i :
                ans = ans*10 + i % 10
                i = i // 10
            return ans
        if x < 0:
            ans = -helper(-x)
        else:
            ans =  helper(x)
        if -2**31 -1< ans < 2**31 -1:
            return ans
        return 0
