for i in range(int(input())):
    A,B,C,D,E=map(int,input().split())
    if A+B<=D and C<=E:
        print('YES')
    elif B+C<=D and A<=E:
        print('YES')
    elif A+C<=D and B<=E:
        print('YES')
    else:
        print('NO')
