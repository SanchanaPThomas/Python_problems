for _ in range(int(input())):
    a,b,c=map(int,input().split())
    total=a+b+c
    maximum=max(a,b,c)
    minimum=min(a,b,c)
    print(total-maximum-minimum)
