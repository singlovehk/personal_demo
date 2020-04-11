#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    diction = {1:1, 2:2, 3:4}
    for i in range(4, n+1):
        diction[i] = diction[i-3] + diction[i-2] + diction[i-1]
    return diction[n] % (10 ** 10 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
