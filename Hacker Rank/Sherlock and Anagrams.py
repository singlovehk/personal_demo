#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    lengths = len(s)
    diction = {l:{} for l in range(1, lengths+1)}
    counts = 0
    for i in range(lengths):
        for j in range(len(s[i:])):
            word = ''.join(sorted(s[i: i+j+1]))
            if word in diction[len(word)].keys():
                counts += diction[len(word)][word]
            diction[len(word)][word] = diction[len(word)].get(word,0) + 1
               
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
