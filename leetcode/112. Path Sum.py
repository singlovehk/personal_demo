class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        cur = []
        def helper(root, prev_sum):
            if not root:
                pass
            elif not root.left and not root.right:
                cur.append(root.val + prev_sum)
            else:
                helper(root.left, root.val + prev_sum)
                helper(root.right, root.val + prev_sum)
        helper(root, 0)
        return sum in cur
