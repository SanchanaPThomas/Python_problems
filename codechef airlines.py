for _ in range(int(input())):
    x,y,z=map(int,input().split())
    m=x*10
    if y>m:
        print(m*z)
    else:
        print(y*z)
