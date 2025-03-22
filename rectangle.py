for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a==b and c==d:
        print('YES')
    elif b==c and a==d:
        print('YES')
    elif b==d and a==c:
        print('YES')
    else:
        print('NO')
