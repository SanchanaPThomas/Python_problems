for i in range(int(input())):
    n,a=map(int,input().split())
    if n-a<a:
        print(n-a)
    else:
        print(a)
