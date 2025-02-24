for _ in range (int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    m=0
    for i in range(n-1):
        m+=(abs(s[i]-s[i+1])-1)
    print(m)
