for _ in range(int(input())):
    x,y=map(int,input().split())
    m=x-y
    k=(x*110)//100
    print(k-m)
