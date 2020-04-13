class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        for i in range(1, len(nums)):
            if 2*sum(nums[:i]) > total:
                return nums[:i]
        return nums
