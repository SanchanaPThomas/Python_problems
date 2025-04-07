from collections import Counter
for _ in range(int(input())):
    s=input()
    char_counts=Counter(s)
    cost=sum((count+1)//2 for count in char_counts.values())
    print(cost)
