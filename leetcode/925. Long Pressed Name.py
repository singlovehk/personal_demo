class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        cur = 0
        while cur < len(name):
            for char in typed:
                if name[cur] == char:
                    cur = cur + 1

                elif name[cur - 1] == char:
                    pass
                else:
                    return False
                if cur == len(name):
                    return True
            
