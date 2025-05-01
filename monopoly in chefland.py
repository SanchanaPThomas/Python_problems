for _ in range(int(input())):
    r1,r2,r3=map(int,input().split())
    if r1+r2<r3 or r1+r3<r2 or r2+r3<r1:
        print('yes')
    else:
        print('no')
