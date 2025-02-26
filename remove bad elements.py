from collections import Counter

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count = Counter(a)
    max_frequency = max(count.values())
    print(n - max_frequency)
        
