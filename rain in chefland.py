for _ in range(int(input())):
    x=int(input())
    if x<3:
        print('light')
    elif 3<=x<7:
        print('moderate')
    elif x>=7:
        print('heavy')
