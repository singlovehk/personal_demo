class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i - 1]
        rev = nums[::-1]
        for i in range(1, n):
            post[i] = post[i-1] * rev[i - 1]
        return [pre[i]* post[-(i +1)] for i in range(n)]
