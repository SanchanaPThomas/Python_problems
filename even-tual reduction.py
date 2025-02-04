for i in range(int(input())):
    n=int(input())
    s=input()
    l=list(s)
    m=set(l)
    for i in m:
        if l.count(i)%2!=0:
            print('NO')
            break
    else:
        print('YES')

