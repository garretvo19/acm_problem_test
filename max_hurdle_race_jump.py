#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
res = max(max(height)-k,0) # use max when there exists a range of values that I can finish 
print(res)