for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    m=w+y*z
    if x>m:
        print('Unfilled')
    elif x<m:
        print('overflow')
    else:
        print('filled')
