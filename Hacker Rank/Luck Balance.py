#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    imp = []
    not_imp = []
    for i, j in contests:
        if j == 0:
            not_imp.append(i)
        else :
            imp.append(i)
    imp.sort(reverse=True)
    return (sum(not_imp) + sum(imp[:k]) - sum(imp[k:]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
