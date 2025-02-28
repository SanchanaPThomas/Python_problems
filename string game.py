for _ in range(int(input())):
    n=int(input())
    s=input()
    s_set=set(s)
    for i in s_set:
        if s.count(i)%2!=0:
            print('NO')
            break
    else:
        print('YES')
