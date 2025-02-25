for _ in range(int(input())):
    n=int(input())
    s=input()
    s_set=set(s)
    for i in s:
        if s.count(i)>=2:
            print(n-2)
            break
    else:
        print(-1)
