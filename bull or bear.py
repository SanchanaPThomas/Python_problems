for _ in range (int(input())):
    x,y=map(int,input().split())
    if y>x:
        print('PROFIT')
    elif y<x:
        print('LOSS')
    else:
        print('NEUTRAL')
