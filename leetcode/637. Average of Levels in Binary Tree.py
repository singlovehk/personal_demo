class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
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
        return [float(sum(i))/float(len(i)) for i in result]
