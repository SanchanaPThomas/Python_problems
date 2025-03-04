for _ in range(int(input())):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    m=[]
    for i in range(n):
        if d[i]%k==0:
            m.append('1')
        else:
            m.append('0')
    print("".join(m))
