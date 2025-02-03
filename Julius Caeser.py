import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    m=list(s)
    n=''
    for i in s:
        if 65<=ord(i)<=90:
            n+=chr((ord(i)-ord('A')+k)%26+ord('A'))
        elif 97<=ord(i)<=122:
            n+=chr((ord(i)-ord('a')+k)%26+ord('a'))
        else:
            n+=i
    return n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

