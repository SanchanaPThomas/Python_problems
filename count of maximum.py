for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a_set=set(a)
    m=0
    k=-1
    for i in a_set:
        if a.count(i)>m:
            m=a.count(i)
            n=i
        elif a.count(i)==m:
            if i<n:
                n=i
    print(n,m)
