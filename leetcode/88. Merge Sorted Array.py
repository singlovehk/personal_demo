class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pt1 = m - 1
        pt2 = n - 1
        pointer = m + n - 1
        while pt1>= 0 and pt2 >=0:
            if nums2[pt2] >= nums1[pt1]:
                nums1[pointer] = nums2[pt2]
                pt2 -= 1
                pointer -= 1
            else:
                nums1[pointer] = nums1[pt1]
                pt1 -= 1
                pointer -= 1
        while pt2 >=0:
            nums1[pointer] = nums2[pt2]
            pt2 -= 1
            pointer -= 1
        
        while pt1 >=0:
            nums1[pointer] = nums1[pt1]
            pt1 -= 1
            pointer -= 1
        return None
