for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    s=0
    for i in b:
        if s<a.count(i):
            s=a.count(i)
            m=i
    l=0
    for j in range(len(a)):
        if a[j]!=m:
            l=l+1
    print(l)
