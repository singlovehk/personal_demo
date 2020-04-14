class Solution(object):
    def pathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        cur = []
        def helper(root, prev_sum):
            if not root:
                pass
            elif not root.left and not root.right:
                cur.append(prev_sum + [root.val])
            else:
                helper(root.left, prev_sum + [root.val])
                helper(root.right, prev_sum + [root.val])
                
        helper(root, [])
        ans = [i for i in cur if sum(i) == sums]
        return ans
