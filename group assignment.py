for _ in range(int(input())):
    N=int(input())
    P=list(map(int,input().split()))
    P_set=set(P)
    for i in P_set:
        m=P.count(i)
        if m%i!=0:
            print('NO')
            break
    else:
        print('YES')
