import math
import os
import random
import re
import sys


def pageCount(n, p):
    if p>n/2:
        if n%2==0 and p%2!=0:
            return ((n-p)//2)+1
        else:
            return (n-p)//2
    else:
        return p//2        


n = int(input('enter the total number of pages').strip())
p = int(input('enter the page to be turned').strip())
print(pageCount(n, p))
