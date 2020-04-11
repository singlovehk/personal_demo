#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    counter = {}

    for ind, v1 in enumerate(cost):
        if money - v1 in counter.keys():
            print('{} {}'.format(counter[money - v1], ind + 1))
        else:
            counter[v1] = ind + 1
        


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
