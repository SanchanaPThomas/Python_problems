for i in range(int(input())):
    x,y,z=map(int,input().split())
    if y<=x:
        print('pizza')
    elif z<=x:
        print('burger')
    else:
        print('nothing')
