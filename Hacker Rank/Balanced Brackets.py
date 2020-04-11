#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    opening = ['(', '[', '{']
    pair = {'(':')', '[':']', '{': '}'}
    nonclose = []
    for i in s:
        if i in opening:
            nonclose.append(i)
        else:
            if len(nonclose) == 0:
                return 'NO'
            cur = nonclose.pop()
            if pair[cur] != i:
                return 'NO'
    if nonclose:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
