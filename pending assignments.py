for _ in range(int(input())):
    x,y,z=map(int,input().split())
    m=x*y
    if m<=z*60:
        print('yes')
    else:
        print('no')
