for _ in range(int(input())):
    x,y=map(int,input().split())
    if x<y:
        print('repair')
    elif x>y:
        print('new phone')
    else:
        print('any')
