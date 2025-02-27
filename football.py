for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m=[]
    for i in range(n):
        s=(a[i]*20)-(b[i]*10)
        m.append(s)
    if max(m)<0:
        print(0)
    else:
        print(max(m))
