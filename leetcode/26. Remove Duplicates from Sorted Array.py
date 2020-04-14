class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur = nums[0]
        cur_ind = 1
        distinct = 1
        for ind, i in enumerate(nums):
            if i > cur:
                nums[cur_ind] = i
                cur_ind += 1
                cur = i
                distinct += 1
        return distinct
