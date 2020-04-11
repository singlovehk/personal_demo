#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    min_day = goal // len(machines) 
    max_day = (goal // len(machines) + 1) * max(machines)
    while max_day > min_day + 1:
        
        mid_day = (max_day + min_day) // 2
        produced = sum(mid_day//x for x in machines)
        if produced >= goal:
            max_day = mid_day
        else:
            min_day = mid_day
    return max_day

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
