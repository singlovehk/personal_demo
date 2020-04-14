# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result = []
        def bfs(node, level):
            if node:
                if len(result) <= level:
                    result.append([])
                result[level].append(node.val)
                bfs(node.left, level + 1)
                bfs(node.right, level + 1)
        bfs(root, 0)
        return result[::-1]
