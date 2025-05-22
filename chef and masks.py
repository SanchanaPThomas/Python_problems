for _ in range(int(input())):
    x,y=map(int,input().split())
    disposable=x*100
    cloth=y*10
    if disposable<cloth:
        print('Disposable')
    else:
        print('Cloth')
