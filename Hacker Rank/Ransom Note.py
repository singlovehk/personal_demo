#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    diction = {}
    for i in magazine:
        diction[i] = diction.get(i, 0) + 1
    for j in note:
        if j not in diction.keys() or diction[j] == 0:
            return 'No'
        else :
            diction[j] -= 1
    return 'Yes'

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
