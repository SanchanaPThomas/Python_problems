for _ in range(int(input())):
    x,y=map(int,input().split())
    m=x*1.07
    if y<=m:
        print('YES')
    else:
        print('NO')
