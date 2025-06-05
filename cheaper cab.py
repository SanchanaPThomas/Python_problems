for _ in range(int(input())):
    x,y=map(int,input().split())
    if x<y:
        print('first')
    elif y<x:
        print('second')
    else:
        print('any')
