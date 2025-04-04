for _ in range(int(input())):
    x,y,n,r=map(int,input().split())
    if n*y<r:
        print(0,n)
    elif n*x>r:
        print(-1)
    else:
         premium_burgers = min(n, (r - n * x) // (y - x))
         normal_burgers = n - premium_burgers
         print(normal_burgers, premium_burgers)
