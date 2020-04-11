#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    if n <= 3:
        return 2 ** (n-1)
    s1 = 1
    s2 = 2
    s3 = 4
    for i in range(4, n+1):
        s1, s2, s3 = s2, s3, s1+s2+s3 % (10**10 + 7)
    return s3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

