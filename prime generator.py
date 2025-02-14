import sys
import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for num in range(a, b + 1):
        if is_prime(num):
            print(num)
    if _ < t - 1:
        print()
