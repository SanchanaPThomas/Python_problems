for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a_set=set(a)
    for i in a_set:
        m=a.count(i)
        if m%2!=0:
            print('NO')
            break
    else:
        print('YES')
