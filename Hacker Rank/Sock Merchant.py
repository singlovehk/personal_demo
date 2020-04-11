#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    ar = sorted(ar)
    i = 0
    while i < len(ar):
        print(i)
        if i + 1 != len(ar) and ar[i] == ar[i+1]:
            i +=  1
            pairs += 1
        i += 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
