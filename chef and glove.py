for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    g=list(map(int,input().split()))
    g_rev=g[::-1]
    f=0
    b=0
    for i in range(n):
        if l[i]<=g[i]:
            f+=1
        if l[i]<=g_rev[i]:
            b+=1
    if f==n and b==n:
        print('both')
    elif f==n:
        print('front')
    elif b==n:
        print('back')
    else:
        print('none')
            
