class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ins = {}
        notin = {}
        
        for i in T:
            if i in S:
                ins[i] = ins.get(i, 0) + 1
            else:
                notin[i] = notin.get(i, 0) + 1
        ans = ''
        for i in S:
            ans = ans + i * ins.get(i, 0)
        for i in notin:
            ans = ans + i * notin[i]
        return ans
