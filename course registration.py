for _ in range(int(input())):
    n,m,k=map(int,input().split())
    if n+k>m:
        print('no')
    else:
        print('yes')
