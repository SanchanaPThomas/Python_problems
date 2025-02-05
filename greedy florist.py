import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
    c.sort()
    l=len(c)
    s=0
    j=0
    for i in range(l-1,-1,-1):
        m=j//k
        s=s+((m+1)*c[i])
        j=j+1
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
