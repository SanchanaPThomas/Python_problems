for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    z=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                s=a[i]*a[j]
                m=sum(map(int,str(s)))
                if m>z:
                    z=m
    print(z)
